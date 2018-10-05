"""Help module for function 9"""
import data_holder,csv,operator
import function_3

min_procurement_dictionary={}
sorted_min_procurement_dictionary_ascending={}
sorted_min_procurement_dictionary_descending={}

def agency_min_procurement():
    """This function creates a dictionary storing the minimum awarded amount for each agency."""
    global min_procurement_dictionary
    string_rep="Data recorded below indicates the minimum procurement amount for each agency:"
    count=0
    signify_end="------END OF CURRENT DATA------"
    try:
        if min_procurement_dictionary=={}:
            function_3.procurement_dictionary1()
            for k,v in function_3.procurement_dictionary.iteritems():
                combined_string= ",".join(str(number) for number in function_3.procurement_dictionary[k])
                store_min=(combined_string).split(",")
                store_min=[round(float(elements),2) for elements in store_min]
                min_procurement_dictionary[k]=min(store_min)
            for rows,value in min_procurement_dictionary.iteritems():
                count +=1
                string_rep = string_rep + "\n" + str(count) + ") " + rows + ": " +str(value)
                if count == len(min_procurement_dictionary):
                    string_rep = string_rep +"\n" + "%050s" %(signify_end)
                    return string_rep
        else:
            for rows,value in min_procurement_dictionary.iteritems():
                count +=1
                string_rep = string_rep + "\n" + str(count) + ") " + rows + ": " +str(value)
                if count == len(min_procurement_dictionary):
                    string_rep = string_rep +"\n" + "%050s" %(signify_end)
                    return string_rep
    except (ValueError,IndexError,ImportError):
        return "Error with value/import/index file."

def sorted_min_procurement(asc):
    """This functions sorts the minimum awarded amount dictionary in ascending/descending order depending on the user's request."""
    global min_procurement_dictionary
    global sorted_min_procurement_dictionary_ascending
    global sorted_min_procurement_dictionary_descending
    total_count =0
    signify_end="------END OF CURRENT DATA------"
    try:
        if asc==True:
            string_rep ="Data recorded below indicates the minimum procurement amount sorted in ascending order for each agency:"
            sorted_min_procurement_dictionary_ascending=sorted(min_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=False)
            for k,v in sorted_min_procurement_dictionary_ascending:
                total_count+=1
                string_rep = string_rep +"\n"+ str(total_count) +") "  +str(k) + ": " + str(v)
                if total_count == len(min_procurement_dictionary):
                    string_rep = string_rep +"\n" + "%050s" %(signify_end)
                    return string_rep
        elif asc== False:
            string_rep ="Data recorded below indicates the minimum procurement amount sorted in descending order for each agency:"
            sorted_min_procurement_dictionary_descending=sorted(min_procurement_dictionary.items(), key=operator.itemgetter(1), reverse= True)
            for k,v in sorted_min_procurement_dictionary_descending:
                total_count+=1
                string_rep = string_rep + "\n"+ str(total_count) +") "  +str(k) + ": " + str(v)
                if total_count == len(min_procurement_dictionary):
                    string_rep = string_rep +"\n" + "%050s" %(signify_end)
                    return string_rep
    except (ValueError,IndexError,ImportError):
        return "Error with value/import/index file."
