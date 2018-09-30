import os
import csv
import shutil

def Create_Folder():
    folder = './Govern Procurement/'
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print ('Error: Creating directory. ' + folder)

def Export_CSV_Data_To_Txt():
    with open ('government-procurement-via-gebiz.csv','r') as csv_file1:
        # fields = [] #initializing

        csv_read = csv.reader(csv_file1) #creating csv reader object
        # extracting field through first row
        # fields = csv_reader.next()

        #write to txt file
        with open('government-procurement-via-gebiz_new.txt', 'w')as csv_file2:
            csv_write = csv.writer(csv_file2, delimiter='\t')
            for items in csv_read:
                csv_write.writerow(items)

        csv_file1.close()

def Save_To_Folder():

    src = os.listdir(r"C:\Users\jia_f\Downloads\rezylana_tnemerucorp_tcejorp_nohtyp-master")
    destination = r"C:\Users\jia_f\Downloads\rezylana_tnemerucorp_tcejorp_nohtyp-master\Govern Procurement"

    for files in src:
        if files.endswith("government-procurement-via-gebiz_new.txt"):
            shutil.move(files,destination)