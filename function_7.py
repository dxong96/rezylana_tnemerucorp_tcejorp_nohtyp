import data_holder,csv,operator
import function_3

no_companies_agency={}
average_procurement ={}
sorted_average_procurement_dictionary_ascending ={}
sorted_average_procurement_dictionary_descending ={}

def agency_no():
    global no_companies_agency
    no_companies_agency={}
    company_count=0
    label=0
    string_rep="Data recorded below indicates the total amount of companies for each agency:"
    signify_end="------END OF CURRENT DATA------"
    for procurement in data_holder.procurements:
        if procurement.agency not in no_companies_agency:
            company_count=1
            no_companies_agency[procurement.agency]=company_count
        elif procurement.agency in no_companies_agency:
            company_count +=1
            no_companies_agency[procurement.agency]=company_count

    for rows,value in no_companies_agency.iteritems():
        label +=1
        string_rep = string_rep +"\n" + str(label) + " " + rows + ": " +str(value)
        if label == len(no_companies_agency):
            string_rep = string_rep +"\n" + "%050s" %(signify_end)
            return string_rep

def average_procurement1():
    global average_procurement
    string_rep="Data recorded below indicates the average procurement amount for each agency:"
    count = 0
    signify_end="------END OF CURRENT DATA------"
    for row in function_3.total_procurement_dictionary:
        average_procurement[row]=round(float(function_3.total_procurement_dictionary[row])/no_companies_agency[row],2)
    for rows,value in average_procurement.iteritems():
        count +=1
        string_rep = string_rep + "\n" + str(count) + " " + rows + ": " +str(value)
        if count == len(average_procurement):
            string_rep = string_rep +"\n" + "%050s" %(signify_end)
            return string_rep
def sorted_average_procurement(asc):
    global average_procurement
    global sorted_average_procurement_dictionary_ascending
    global sorted_average_procurement_dictionary_descending
    total_count =0
    signify_end="------END OF CURRENT DATA------"
    if asc==True:
        string_rep="Data recorded below indicates the sorted average amount for each agency in ascending order:"
        sorted_average_procurement_dictionary_ascending=sorted(average_procurement.items(), key=operator.itemgetter(1) ,reverse=False)
        for k,v in sorted_average_procurement_dictionary_ascending:
            total_count+=1
            string_rep = string_rep + "\n" + str(total_count) +") "  +str(k) + ": " + str(v)
            if total_count == len(sorted_average_procurement_dictionary_ascending):
                string_rep = string_rep +"\n" + "%050s" %(signify_end)
                return string_rep
    elif asc== False:
        string_rep="Data recorded below indicates the sorted average amount for each agency in descending order:"
        sorted_average_procurement_dictionary_descending=sorted(average_procurement.items(), key=operator.itemgetter(1), reverse= True)
        for k,v in sorted_average_procurement_dictionary_descending:
            total_count+=1
            string_rep = string_rep + "\n" + str(total_count) +") "  +str(k) + ": " + str(v)
            if total_count == len(sorted_average_procurement_dictionary_descending):
                string_rep = string_rep +"\n" + "%050s" %(signify_end)
                return string_rep

