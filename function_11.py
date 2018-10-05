"""Help module for function 11"""
import data_holder,csv,datetime,operator

storage_date={}
expired_storage_date={}
expired_storage_date_ascending={}
expired_storage_date_descending={}


def sort_date_time1():
    """This function creates 2 dictionaries, one of which stores company that hasnt expired and one of which that expired."""
    global storage_date
    global expired_storage_date
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day=now.day
    count =0
    string_rep_expired=""
    string_rep=""
    expired_count=1
    valid_count=1
    try:
        if storage_date=={} and expired_storage_date=={}:
            with open(data_holder.contractors_source_path,"r") as csvfile1:
                reader = csv.reader(csvfile1)
                for row in reader:
                    if count > 0:
                        year_holder1="".join(row[5])
                        year_holder=year_holder1.split("/")
                        if int(year) > int(year_holder[2]):
                            string_rep_expired=string_rep_expired+ "\n" +str(expired_count)+ ") "+ "This procurement owned by " + str(row[0].lower()) +" (workhead number:) " +row[2] + " has expired on " + row[5]+"."
                            expired_count += 1
                            expired_storage_date[(row[0],row[2])]=row[5]
                        elif int(year) == int(year_holder[2]):
                            if int(month) > int(year_holder[1]):
                                string_rep_expired = string_rep_expired +"\n" +str(expired_count)+ ") " +"This procurement owned by " + str(row[0].lower()) +" (workhead number:) " +row[2] + " has expired on " + row[5]+"."
                                expired_count +=1
                                expired_storage_date[(row[0],row[2])]=row[5]
                            elif int(month) == int(year_holder[1]):
                                if int(day) > int(year_holder[0]) or int(day) == int(year_holder[0]):
                                    string_rep_expired = string_rep_expired + "\n" +str(expired_count)+ ") "+ "This procurement owned by " + str(row[0].lower()) +" (workhead number:) " +row[2] + " has expired on " + row[5]+"."
                                    expired_count += 1
                                    expired_storage_date[(row[0],row[2])]=row[5]
                                else:
                                    string_rep = string_rep +"\n" +str(valid_count)+") "+" This procurement owned by " + str(row[0].lower()) +" (workhead number:) " +row[2] + " has not expired, it will only be expiring on " + row[5]+"."
                                    valid_count +=1
                                    storage_date[(row[0],row[2])]=row[5]
                            else:
                                string_rep = string_rep +"\n" + str(valid_count)+") "+ "This procurement owned by " + str(row[0].lower()) +" (workhead number:) " +row[2] + " has not expired, it will only be expiring on " + row[5]+"."
                                valid_count +=1
                                storage_date[(row[0],row[2])]=row[5]
                        else:
                            string_rep = string_rep +"\n" + str(valid_count)+") "+ " This procurement owned by " + str(row[0].lower()) +" (workhead number:) " +row[2] + " has not expired, it will only be expiring on " + row[5]+"."
                            valid_count +=1
                            storage_date[(row[0],row[2])]=row[5]
                            count+=1
                    else:
                        count +=1
                return string_rep
        else:
            return string_rep
    except (ValueError,IndexError,ImportError):
        return "Error with value/import/index file."

def sort_by_expired_date1(asc):
    """This function sorts the dictionary containing expired company by date"""
    global expired_storage_date
    total_count=0
    signify_end="------END OF CURRENT DATA------"
    try:
        if asc==True:
            string_rep = "Data recorded below indicates expired companies that is arranged according to the date in ascending order:"
            for row,value in expired_storage_date.iteritems():
                expired_storage_date_ascending[row]=expired_storage_date[row]
                expired_storage_date_ascending[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
            for k,v in sorted(expired_storage_date_ascending.items(), key=operator.itemgetter(1), reverse=False):
                total_count += 1
                string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
                if total_count == len(expired_storage_date_ascending):
                    string_rep = string_rep + "\n" + "%050s" %(signify_end)
            return string_rep
        elif asc==False:
            string_rep = "Data recorded below indicates expired companies that is arranged according to the date in descending order:"
            for row,value in expired_storage_date.iteritems():
                expired_storage_date_descending[row]=expired_storage_date[row]
                expired_storage_date_descending[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
            for k,v in sorted(expired_storage_date_descending.items(), key=operator.itemgetter(1), reverse=True):
                total_count += 1
                string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
                if total_count == len(expired_storage_date_descending):
                    string_rep = string_rep + "\n" + "%050s" %(signify_end)
            return string_rep
    except (ValueError,IndexError,ImportError):
        return "Error with value/import/index file."
