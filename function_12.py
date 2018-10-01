import data_holder,csv,datetime,operator
import function_11

listing1="C:/Users/bry/Downloads/Project Datasets/listing-of-registered-contractors/listing-of-registered-contractors.csv"


def sort_by_nonexpired_date1(asc):
    global storage_date
    total_count = 0
    signify_end = "------END OF CURRENT DATA------"
    if asc == True:
        string_rep = "Data recorded below indicates companies that hasnt expired that are arranged according to the date in ascending order:"
        for row, value in function_11.storage_date.iteritems():
            function_11.storage_date[row] = datetime.datetime.strptime(value, "%d/%m/%Y").strftime("%Y/%m/%d")
            for k, v in sorted(function_11.storage_date.items(), key=operator.itemgetter(1), reverse=False):
                total_count += 1
                string_rep = string_rep + "\n" + str(total_count) + ") " + str(k) + ": " + str(v)
                if total_count == len(function_11.storage_date):
                    string_rep = string_rep + "\n" + "%050s" % (signify_end)
                    return string_rep
    elif asc == False:
        string_rep = "Data recorded below indicates companies that hasnt expired that are arranged according to the date in descending order:"
        for row, value in function_11.storage_date.iteritems():
            function_11.storage_date[row] = datetime.datetime.strptime(value, "%d/%m/%Y").strftime("%Y/%m/%d")
            for k, v in sorted(function_11.storage_date.items(), key=operator.itemgetter(1), reverse=True):
                total_count += 1
                string_rep = string_rep + "\n" + str(total_count) + ") " + str(k) + ": " + str(v)
                if total_count == len(function_11.storage_date):
                    string_rep = string_rep + "\n" + "%050s" % (signify_end)
                    return string_rep