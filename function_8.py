"""Help module for function 8"""
import data_holder,csv,operator
import function_3

max_procurement_dictionary={}
sorted_max_procurement_dictionary_ascending={}
sorted_max_procurement_dictionary_descending={}


def agency_max_procurement():
    """This function creates a dictionary storing the max awarded amount for each agency"""
    global max_procurement_dictionary
    string_rep="Data recorded below indicates the maximum procurement amount for each agency:"
    count =0
    signify_end="------END OF CURRENT DATA------"
    try:
        if max_procurement_dictionary=={}:
            function_3.procurement_dictionary1()
            for k,v in function_3.procurement_dictionary.iteritems():
                combined_string= ",".join(str(number) for number in function_3.procurement_dictionary[k])
                store_max=(combined_string).split(",")
                store_max=[round(float(elements),2) for elements in store_max]
                max_procurement_dictionary[k]=max(store_max)
            for rows,value in max_procurement_dictionary.iteritems():
                count+=1
                string_rep = string_rep + "\n" + str(count) + ") " + rows + ": " +str(value)
                if count == len(max_procurement_dictionary):
                    string_rep = string_rep +"\n" + "%050s" %(signify_end)
                    return string_rep
        else:
            for rows, value in max_procurement_dictionary.iteritems():
                count += 1
                string_rep = string_rep + "\n" + str(count) + ") " + rows + ": " + str(value)
                if count == len(max_procurement_dictionary):
                    string_rep = string_rep + "\n" + "%050s" % (signify_end)
                    return string_rep
    except (ValueError,IndexError,ImportError):
        return "Error with value/import/index file."

def sorted_max_procurement(asc):
    """This function sorts the max awarded amount in ascending/descending order depending on the user's request."""
    global max_procurement_dictionary
    global sorted_max_procurement_dictionary_ascending
    global sorted_max_procurement_dictionary_descending
    total_count =0
    signify_end="------END OF CURRENT DATA------"
    try:
        if asc==True:
            string_rep ="Data recorded below indicates the max procurement amount sorted in ascending order for each agency:"
            sorted_max_procurement_dictionary_ascending=sorted(max_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=False)
            for k,v in sorted_max_procurement_dictionary_ascending:
                total_count+=1
                string_rep = string_rep + "\n" +str(total_count) +") "  +str(k) + ": " + str(v)
                if total_count == len(max_procurement_dictionary):
                    string_rep = string_rep +"\n" + "%050s" %(signify_end)
                    return string_rep
        elif asc==False:
            string_rep ="Data recorded below indicates the max procurement amount sorted in descending order for each agency:"
            sorted_max_procurement_dictionary_descending=sorted(max_procurement_dictionary.items(), key=operator.itemgetter(1), reverse= True)
            for k,v in sorted_max_procurement_dictionary_descending:
                total_count+=1
                string_rep = string_rep +"\n"+ str(total_count) +") "  +str(k) + ": " + str(v)
                if total_count == len(max_procurement_dictionary):
                    string_rep = string_rep +"\n" + "%050s" %(signify_end)
                    return string_rep
    except (ValueError,IndexError,ImportError):
        return "Error with value/import/index file."
