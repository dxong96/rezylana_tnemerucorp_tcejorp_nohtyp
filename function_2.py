'''Read the CSV file and export each government agency's procurement details into one folder and sort the details by tender number in txt file'''

import os
import data_holder
import tkMessageBox

def Create_Folder():
    '''Create Govern Procurement Folder'''
    folder = './Govern Procurement/'                                                                  #Folder name Govern Procurement
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)                                                                       #If folder does not exists then create folder
    except OSError:
        tkMessageBox.showinfo("Error", 'Error creating directory. ' + folder)                         #Error message dialog box pop out if folder exist

def save():
    '''Create Govern procurements folder & save the procurements details for agency into txt file in Govern Procurement folder'''
    try:
        Create_Folder()
        agency_to_procurements = data_holder.create_dict_for_list(data_holder.procurements, 'agency') #Create dictionary to store procurement information

        for agency in agency_to_procurements:
            folder = './Govern Procurement/'
            file_path = folder + '%s.txt' % agency                                                    #Convert government-procurement-via-gebiz csv file to txt file, and save the txt file to Govern Procurement folder
            with open(file_path, 'w') as f:                                                           #Open the txt file as writable file
                for procurement in agency_to_procurements[agency]:
                    f.write(procurement.display_text() + '\n')                                        #Display the procurement details in text

                    f.write('='*1000 + '\n')                                                          #Divider

        tkMessageBox.showinfo("Message", "File save to Govern Procurement folder successful")         #Message dialog box pop out when file save successful

    except:
        tkMessageBox.showinfo("Error", "Unable to save file")                                         #Error message dialog box pop out when file was not save successful
