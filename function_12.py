"""Help module for function 12"""
import data_holder,csv,datetime,operator
import function_11
storage_date_ascending={}
storage_date_descending={}

def sort_by_nonexpired_date1(asc):
    """This function sorts the dictionary containing non-expired companies by date"""
    global storage_date_ascending
    global storage_date_descending
    total_count=0
    signify_end="------END OF CURRENT DATA------"
    try:
        if function_11.storage_date=={}:
            function_11.sort_date_time1()
            if asc==True:
                string_rep = "Data recorded below indicates non-expired companies that is arranged according to the date in ascending order:"
                for row,value in function_11.storage_date.iteritems():
                    storage_date_ascending[row]=function_11.storage_date[row]
                    storage_date_ascending[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
                for k,v in sorted(storage_date_ascending.items(), key=operator.itemgetter(1), reverse=False):
                    total_count += 1
                    string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
                    if total_count == len(storage_date_ascending):
                        string_rep = string_rep + "\n" + "%050s" %(signify_end)
                return string_rep
            elif asc==False:
                string_rep = "Data recorded below indicates non-expired companies that is arranged according to the date in descending order:"
                for row,value in function_11.storage_date.iteritems():
                    storage_date_descending[row] = function_11.storage_date[row]
                    storage_date_descending[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
                for k,v in sorted(storage_date_descending.items(), key=operator.itemgetter(1), reverse=True):
                    total_count += 1
                    string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
                    if total_count == len(storage_date_descending):
                        string_rep = string_rep + "\n" + "%050s" %(signify_end)
                return string_rep
        else:
            if asc==True:
                string_rep = "Data recorded below indicates non-expired companies that is arranged according to the date in ascending order:"
                for row,value in function_11.storage_date.iteritems():
                    storage_date_ascending[row]=function_11.storage_date[row]
                    storage_date_ascending[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
                for k,v in sorted(storage_date_ascending.items(), key=operator.itemgetter(1), reverse=False):
                    total_count += 1
                    string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
                    if total_count == len(storage_date_ascending):
                        string_rep = string_rep + "\n" + "%050s" %(signify_end)
                return string_rep
            elif asc==False:
                string_rep = "Data recorded below indicates non-expired companies that is arranged according to the date in descending order:"
                for row,value in function_11.storage_date.iteritems():
                    storage_date_descending[row] = function_11.storage_date[row]
                    storage_date_descending[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
                for k,v in sorted(storage_date_descending.items(), key=operator.itemgetter(1), reverse=True):
                    total_count += 1
                    string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
                    if total_count == len(storage_date_descending):
                        string_rep = string_rep + "\n" + "%050s" %(signify_end)
                return string_rep
    except (ValueError,IndexError,ImportError):
        return "Error with value/import/index file."
