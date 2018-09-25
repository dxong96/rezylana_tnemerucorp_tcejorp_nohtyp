import csv
from classes import Contractor
from classes import Procurement

contractors = []
procurements = []

def load_contractor_list(path):
    new_contractors = []
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            # check line for commas to ensure
            contractor = Contractor(row)
            new_contractors.append(contractor)
        f.close()

    global contractors # we need to write global to be able to assign to the module variables
    contractors = new_contractors


def load_procurement_list(path):
    count = 0  #bryan added this in to skip the first row, not sure if correct
    new_procurements = []
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if count > 0:
                # check line for commas to ensure
                procurement = Procurement(row)
                new_procurements.append(procurement)
            else:
                count+=1
        f.close()
    
    global procurements
    procurements = new_procurements

def create_dict_for_list(items, key):
    result = {}
    for item in items:
        result[getattr(item, key)] = item
    return result

def are_sheets_loaded():
    return len(contractors) > 0 and len(procurements) > 0
