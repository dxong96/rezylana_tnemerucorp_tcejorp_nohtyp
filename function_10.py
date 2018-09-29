import data_holder,csv,operator

listing1="C:/Users/bry/Downloads/Project Datasets/listing-of-registered-contractors/listing-of-registered-contractors.csv"

contractor_workhead_grade_dictionary={}
tuple_of_all_companies=()

def contractor_workhead_grade():
    global contractor_workhead_grade_dictionary
    global tuple_of_all_companies
    count = 0
    total_count =0
    signify_end="------END OF CURRENT DATA------"
    string_rep="Data recorded below indicates the grades related to each company and it's workhead:"
    with open(listing1,"r") as csvfile1:
        reader = csv.reader(csvfile1)
        for row in reader:
            if count > 0:
                count+=1
                tuple_of_all_companies=(row[0],row[2])
                contractor_workhead_grade_dictionary[(row[0],row[2])]=row[3]
            else:
                count +=1
        for k,v in contractor_workhead_grade_dictionary.iteritems():
            k1 = ",".join(k)
            total_count += 1
            string_rep = string_rep + "\n"+ str(total_count)+ ") "+ str(k1)+ ": " + str(v)
            if total_count == len(contractor_workhead_grade_dictionary):
                string_rep = string_rep + "\n" + "%050s" %(signify_end)

        return string_rep