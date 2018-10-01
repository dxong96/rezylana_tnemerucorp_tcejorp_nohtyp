import data_holder,csv,datetime,operator

storage_date={}
expired_storage_date={}

def sort_date_time1():
    global storage_date
    global expired_storage_date
    storage_date={}
    expired_storage_date={}
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day=now.day
    count =0
    string_rep_expired=""
    string_rep=""
    expired_count=1
    valid_count=1
    for contractors in data_holder.contractors:
        year_holder1="".join(contractors.expiry_date)
        year_holder=year_holder1.split("/")
        if int(year) > int(year_holder[2]):
            string_rep_expired=string_rep_expired+ "\n" +str(expired_count)+ ") "+ "This procurement owned by " + str(contractors.company_name.lower()) +" (workhead number:) " +contractors.workhead + " has expired on " + contractors.expiry_date+"."
            expired_count += 1
            expired_storage_date[(contractors.company_name,contractors.workhead)]=contractors.expiry_date
        elif int(year) == int(year_holder[2]):
            if int(month) > int(year_holder[1]):
                string_rep_expired = string_rep_expired +"\n" +str(expired_count)+ ") " +"This procurement owned by " + str(contractors.company_name.lower()) +" (workhead number:) " +contractors.workhead + " has expired on " + contractors.expiry_date+"."
                expired_count +=1
                expired_storage_date[(contractors.company_name, contractors.workhead)] = contractors.expiry_date
            elif int(month) == int(year_holder[1]):
                if int(day) > int(year_holder[0]):
                    string_rep_expired = string_rep_expired + "\n" +str(expired_count)+ ") "+ "This procurement owned by " + str(contractors.company_name.lower()) +" (workhead number:) " +contractors.workhead + " has expired on " + contractors.expiry_date+"."
                    expired_count += 1
                    expired_storage_date[(contractors.company_name, contractors.workhead)] = contractors.expiry_date
                else:
                    string_rep = string_rep +"\n" +str(valid_count)+") "+" This procurement owned by " + str(contractors.company_name.lower()) +" (workhead number:) " +contractors.workhead + " has not expired, it will only be expiring on " + contractors.expiry_date+"."
                    valid_count +=1
                    storage_date[(contractors.company_name, contractors.workhead)] = contractors.expiry_date
            else:
                string_rep = string_rep +"\n" + str(valid_count)+") "+ "This procurement owned by " + str(contractors.company_name.lower()) +" (workhead number:) " +contractors.workhead + " has not expired, it will only be expiring on " + contractors.expiry_date+"."
                valid_count +=1
                storage_date[(contractors.company_name, contractors.workhead)] = contractors.expiry_date
        else:
            string_rep = string_rep +"\n" + str(valid_count)+") "+ " This procurement owned by " + str(contractors.company_name.lower()) +" (workhead number:) " +contractors.workhead + " has not expired, it will only be expiring on " + contractors.expiry_date+"."
            valid_count +=1
            storage_date[(contractors.company_name, contractors.workhead)] = contractors.expiry_date
            count+=1
    return string_rep
def sort_by_expired_date1(asc):
    global expired_storage_date
    total_count=0
    signify_end="------END OF CURRENT DATA------"
    if asc==True:
        string_rep = "Data recorded below indicates expired companies that is arranged according to the date in ascending order:"
        for row,value in expired_storage_date.iteritems():
            expired_storage_date[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
        for k,v in sorted(expired_storage_date.items(), key=operator.itemgetter(1), reverse=False):
            total_count += 1
            string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
            if total_count == len(expired_storage_date):
                string_rep = string_rep + "\n" + "%050s" %(signify_end)
        return string_rep
    elif asc==False:
        string_rep = "Data recorded below indicates expired companies that is arranged according to the date in descending order:"
        for row,value in expired_storage_date.iteritems():
            expired_storage_date[row]=datetime.datetime.strptime(value,"%d/%m/%Y").strftime("%Y/%m/%d")
        for k,v in sorted(expired_storage_date.items(), key=operator.itemgetter(1), reverse=True):
            total_count += 1
            string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k)+ ": " + str(v)
            if total_count == len(expired_storage_date):
                string_rep = string_rep + "\n" + "%050s" %(signify_end)
        return string_rep
