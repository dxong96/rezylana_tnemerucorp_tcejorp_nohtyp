import data_holder
import operator

def generate_stats():
    """
    make a dict in the following format
    {
        company_name: contractor
    }
    """
    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
    procurement_list = data_holder.procurements
    procurement_count_dict = {}
    registered_contractors_names = set()
    unregistered_contractors_count = 0
    for procurement in procurement_list:
        if not procurement.awarded: # skip if it is not awarded to anyone
            continue
        if (procurement.supplier_name in contractor_dict): # a registered contractor
            registered_contractors_names.add(procurement.supplier_name)
        else: # a unregistered contractor
            unregistered_contractors_count += 0

        if (not procurement.supplier_name in procurement_count_dict): # when the dictionary do not have the company name as key
            procurement_count_dict[procurement.supplier_name] = 0 # we initialize it to zero so we can add on to it later
        procurement_count_dict[procurement.supplier_name] += 1

    sorted_company_names = sorted(procurement_count_dict.keys(), \
                                     key=procurement_count_dict.get, \
                                     reverse=True) # sort keys in descending order based on value of a given key
    top_5_company_names = sorted_company_names[:5]

    result = []
    result.append('Registered contractors:')

    result.extend(registered_contractors_names)
    result.append('====')
    result.append('Top 5 companies with the most tenders:')

    top_5_company_name_and_tenders = map(lambda name: \
            '%s with %d tenders' % (name, procurement_count_dict[name]), top_5_company_names)
    result.extend(top_5_company_name_and_tenders)

    result.append('====')
    result.append('Number of unregistered contractors: %d' \
                  % unregistered_contractors_count)
    result.append('====')
    result.append('Number of registered contractors: %d' \
                  % len(registered_contractors_names))
    result.append(procurement_dictionary1())
    result.append(total_procurement_dictionary1())
    result.append(largest_5())
    result.append(smallest_5())
    result.append(sorter(False))

    return '\n'.join(result)

total_procurement_dictionary={} #Represents total procurement amount for each agency
procurement_dictionary={} #Represents procurement amount for each agency


def procurement_dictionary1(): # Used to create procurement dictionary
    global procurement_dictionary
    string = ""
    count =0
    for procurement in data_holder.procurements:
        string += procurement.agency + ": " + str(procurement.awarded_amt) + "\n"
        procurement_dictionary.setdefault(procurement.agency, []).append(round(float(procurement.awarded_amt),2)) #Create dictionary where all procurements are stored in list
    return string

    #return procurement_dictionary

def total_procurement_dictionary1(): #Used to create a dictionary that represents TOTAL procurement amount for each agency
    global total_procurement_dictionary
    string=""
    for k,v in procurement_dictionary.iteritems():
        total = 0
        for number in v: #finding total for each agency and storing it into a new list
            total = round(float(number),2) + total #rounding to 2 decimal place
            total_procurement_dictionary[k]=(round(total,2))
    for rows,value in total_procurement_dictionary.iteritems(): #Putting dictionary values into string
        string = string + rows + ": " +str(value)+ "\n"
    return string
    #return total_procurement_dictionary

def sorter(x):
    news=""
    total_count=0
    if x == True:
        sorted_total_procurement_dictionary= sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=False)
        for item in (sorted_total_procurement_dictionary):
            total_count += 1
            news = news +"#"+str(total_count) + str(item) +"\n"
        return (news)
        #return sorted_total_procurement_dictionary
    elif x == False:
        sorted_total_procurement_dictionary= sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=True)
        for item in (sorted_total_procurement_dictionary):
            total_count +=1
            news = news +"#"+str(total_count) + str(item) +"\n"
        return news
        #return sorted_total_procurement_dictionary

def largest_5():
    top_5descending={}
    count =0
    string_rep=""
    total_count = 0
    for k,v in sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=True):
        if count < 5:
            top_5descending[k]=v
            count +=1
        else:
            break
    for item in sorted(top_5descending.items(), key=operator.itemgetter(1) ,reverse=True):
        total_count +=1
        string_rep = string_rep + str(total_count) +str(item) + "\n"
    return "These are the top 5 highest awarded amount in descending order: " +"\n" + string_rep

def smallest_5():
    count = 0
    smallest_5ascending={}
    string_rep=""
    total_count =0
    for k,v in sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=False):
        if count < 5:
            smallest_5ascending[k]=v
            count +=1
        else:
            break
    for item in sorted(smallest_5ascending.items(), key=operator.itemgetter(1) ,reverse=False):
        total_count +=1
        string_rep = string_rep + str(total_count) + str(item) + "\n"
    return "These are the top 5 lowest awarded amount in ascending order: " +"\n" + string_rep
