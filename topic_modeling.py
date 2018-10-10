"""
The module that contains the class with logic to create the LDA model for procurements.
"""
import data_holder
import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from gensim.utils import simple_tokenize

from nltk import download as nltk_download
import os
import json


class TopicModeller:
    """
    This class creates the LDA model from the procurements from the excel sheet
    Grouped the procurements into the created topics
    Create cached json file of the result

    The result is cached for performance purpose as the training process takes some time.
    """
    cache_most_common_words = None
    grouped_topic_procurements = None

    def __init__(self):
        self.CACHE_JSON_FILE_NAME = 'cached_tender_no_by_topic.json'

    def lemmatize_stemming(self, text):
        """
        Extract the common letters between different from such as
        past tense
        adjective
        plural
         """
        stemmer = SnowballStemmer('english')
        return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    def preprocess(self, text):
        """
        Filter out unwanted words, lowercase, lemmatize to make it easy to match
        :param text:
        :return: list
        """
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
        """
        Create the LDA model with procurements and their tender descriptions.
        Grouped the procurements by the generated topics
        Dump it to a cache json file
        :return: None
        """
        nltk_download('wordnet')
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
        """
        Find the most common words in the procurement tender descriptions.
        Then return top 12 for the top most common words
        :return: List of String
        """
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
        """
        Checks if cache file exists
        :return: True or False
        """
        return not os.path.exists(self.CACHE_JSON_FILE_NAME)

    def group_topic_procurements(self, tender_nos_by_topics):
        """
        Convert tender numbers grouped by their topics to procurements grouped by topic
        then assigned the variable grouped_topic_procurements
        :param tender_nos_by_topics:
        :return: None
        """
        tender_no_to_procurements = data_holder.create_dict_for_list(data_holder.procurements, 'tender_no')
        self.grouped_topic_procurements = []
        for i in range(len(tender_nos_by_topics)):
            topics = tender_nos_by_topics[i]
            procurements = map(lambda t: tender_no_to_procurements[t][0], topics)
            self.grouped_topic_procurements.append(procurements)

    def load_cache_file(self):
        """
        Load the cached file into the class
        :return: None
        """
        with open(self.CACHE_JSON_FILE_NAME, 'r') as f:
            tender_nos_by_topics = json.load(f)
            self.group_topic_procurements(tender_nos_by_topics)

    def clear_cache_file(self):
        """
        Delete the cached file
        :return: None
        """
        if not self.needs_training():
            os.remove(self.CACHE_JSON_FILE_NAME)

    def load_topic_and_procurements(self):
        """
        Decides to load from cache or train a new LDA model
        :return: None
        """
        if self.needs_training():
            self.train()
        else:
            self.load_cache_file()
