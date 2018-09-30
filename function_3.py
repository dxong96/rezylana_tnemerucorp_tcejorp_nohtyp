import data_holder,csv,operator


procurement_dictionary ={}
total_procurement_dictionary={}

def procurement_dictionary1():
    global procurement_dictionary
    procurement_dictionary={}
    string_rep = "Data recorded below indicates the individual procurement amount for each agency:"
    signify_end="------END OF CURRENT DATA------"
    total_count=0
    for procurement in data_holder.procurements:
        # this is so the first row which are all headers arent used
        procurement_dictionary.setdefault(procurement.agency,[]).append(round(float(procurement.awarded_amt),2))
        #creating a dictionary where the values to a key is stored in a list, so for each similar string the value will be appended to that list.
    for rows,value in procurement_dictionary.iteritems():
        total_count +=1
        string_rep = string_rep+"\n"+str(total_count) +") " + rows + ": " +str(value)
        if total_count == len(procurement_dictionary):
            string_rep = string_rep +"\n" + "%050s" %(signify_end)
            return string_rep

def total_procurement_dictionary1():
    global total_procurement_dictionary
    string_rep="Data recorded below indicates the total procurement amount for each agency:"
    count=0
    signify_end="------END OF CURRENT DATA------"
    for k,v in procurement_dictionary.iteritems():
        total = 0
        # set total to 0 at this position so for each new category the total will start afresh at 0.
        for number in v:
            #finding total for each "category" and storing it into a new list
            total = round(float(number),2) + total
            #rounding to 2 decimal place
            total_procurement_dictionary[k]=(round(total,2))
    for rows,value in total_procurement_dictionary.iteritems():
        count +=1
        string_rep = string_rep +"\n" + str(count)+") " + rows + ": " +str(value)
        if count == len(total_procurement_dictionary):
            string_rep = string_rep +"\n" + "%050s" %(signify_end)
            return string_rep

def sorted_total_procurement_dictionary1(asc):
    total_count=0
    signify_end="------END OF CURRENT DATA------"
    if asc==True:
        string_rep="Data recorded below indicates the sorted total amount for each agency in ascending order:"
        sorted_total_procurement_dictionary= sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=False)
        for k,v in sorted_total_procurement_dictionary:
            total_count+=1
            string_rep = string_rep +"\n"+ str(total_count) +") "  +str(k) + ": " + str(v)
            if total_count == len(total_procurement_dictionary):
                string_rep = string_rep +"\n" + "%050s" %(signify_end)
                return string_rep
    elif asc == False:
        string_rep="Data recorded below indicates the sorted total amount for each agency in descending order:"
        sorted_total_procurement_dictionary= sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=True)
        for k,v in sorted_total_procurement_dictionary:
            total_count+=1
            string_rep = string_rep +"\n"+ str(total_count) +") "  +str(k) + ": " + str(v)
            if total_count == len(total_procurement_dictionary):
                string_rep = string_rep +"\n" + "%050s" %(signify_end)
                return string_rep
    else:
        return "error"

