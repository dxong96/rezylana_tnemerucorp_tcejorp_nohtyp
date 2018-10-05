import data_holder
import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from gensim.utils import simple_tokenize

import nltk
import os
import json

class TopicModeller:
    cache_most_common_words = None
    grouped_topic_procurements = None

    def __init__(self):
        self.CACHE_JSON_FILE_NAME = 'cached_tender_no_by_topic.json'

    def lemmatize_stemming(self, text):
        stemmer = SnowballStemmer('english')
        return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    def preprocess(self, text):
        result = []
        common_words = self.most_common_words()
        stop_words = []
        stop_words.extend(gensim.parsing.preprocessing.STOPWORDS)
        stop_words.extend(common_words)
        for token in gensim.utils.simple_preprocess(text):
            if token not in stop_words and len(token) > 2:
                result.append(self.lemmatize_stemming(token))
        return result

    def train(self):
        nltk.download('wordnet')
        processed_tender_descriptions = map(lambda p: self.preprocess(p.tender_description), data_holder.procurements)
        dictionary = gensim.corpora.Dictionary(processed_tender_descriptions)

        dictionary.filter_extremes(no_above=0.25)
        bow_corpus = [dictionary.doc2bow(doc) for doc in processed_tender_descriptions]
        print len(bow_corpus)

        lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary, passes=2, workers=2)

        topic_to_procurements = []
        for i in range(10):
            topic_to_procurements.append([])

        for p in data_holder.procurements:
            unseen_document = p.tender_description
            bow_vector = dictionary.doc2bow(self.preprocess(unseen_document))

            sorted_probabilities = sorted(lda_model[bow_vector], key=lambda tup: -1 * tup[1])
            topic_with_highest_prob = sorted_probabilities[0]
            topic_index = topic_with_highest_prob[0]
            topic_to_procurements[topic_index].append(p.tender_no)

        self.group_topic_procurements(topic_to_procurements)
        with open(self.CACHE_JSON_FILE_NAME, 'w') as outfile:
            json.dump(topic_to_procurements, outfile)

    def most_common_words(self):
        if self.cache_most_common_words is None:
            word_counts = {}
            for p in data_holder.procurements:
                for token in simple_tokenize(p.tender_description.lower()):
                    if token in gensim.parsing.preprocessing.STOPWORDS:
                        continue

                    word_counts.setdefault(token, 0)
                    word_counts[token] += 1

            sorted_keys = sorted(word_counts.keys(), key=word_counts.get, reverse=True)
            self.cache_most_common_words = sorted_keys[:12]
        return self.cache_most_common_words

    def needs_training(self):
        return not os.path.exists(self.CACHE_JSON_FILE_NAME)

    def group_topic_procurements(self, tender_nos_by_topics):
        tender_no_to_procurements = data_holder.create_dict_for_list(data_holder.procurements, 'tender_no')
        self.grouped_topic_procurements = []
        for i in range(len(tender_nos_by_topics)):
            topics = tender_nos_by_topics[i]
            procurements = map(lambda t: tender_no_to_procurements[t][0], topics)
            self.grouped_topic_procurements.append(procurements)

    def load_cache_file(self):
        with open(self.CACHE_JSON_FILE_NAME, 'r') as f:
            tender_nos_by_topics = json.load(f)
            self.group_topic_procurements(tender_nos_by_topics)

    def clear_cache_file(self):
        if not self.needs_training():
            os.remove(self.CACHE_JSON_FILE_NAME)

    def load_topic_and_procurements(self):
        if self.needs_training():
            self.train()
        else:
            self.load_cache_file()