import data_holder
import os


def createFolder():
    test = './new python2/'
    try:
        if not os.path.exists(test):
            os.makedirs(test)
    except OSError:
        print ('Error: Creating directory. ' + test)

agencylist = []
# Example
def writetxt():
    for i in agencylist:
        file = open(os.path.join(test,i+".txt", "w"))
        file.write(i)
        file.write("This is our next text file")
        file.write("and this is anotherline.")
        file.write("Why? Because we can.")

        file.close()


def txtdetails():
    agency_to_procurements = data_holder.create_dict_for_list(data_holder.procurements, 'agency')
    for agency in agency_to_procurements:
        agencylist.append(agency)
        # print agency

