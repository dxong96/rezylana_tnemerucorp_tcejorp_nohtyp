import csv
import json
from classes import Contractor
from classes import Procurement

contractors = []
procurements = []
contractor_registry = False

def load_contractor_list(path):
    contractor_dict = {}
    with open(path, 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            company_name = row['company_name']
            if company_name in contractor_dict:
                contractor = contractor_dict[company_name]
                contractor.add_workhead(row['workhead'], row['grade'])
            else:
                contractor = Contractor(row)
                contractor_dict[company_name] = contractor


        f.close()

    global contractors # we need to write global to be able to assign to the module variables
    contractors = contractor_dict.values()


def load_procurement_list(path):
    new_procurements = []
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        reader.next() # read the next row therefore skipping the first row
        for row in reader:
            # check line for commas to ensure
            procurement = Procurement(row)
            new_procurements.append(procurement)
        f.close()
    
    global procurements
    procurements = new_procurements

def create_dict_for_list(items, key):
    result = {}
    for item in items:
        result.setdefault(getattr(item, key), [])
        result[getattr(item, key)].append(item)
    return result

def are_sheets_loaded():
    return len(contractors) > 0 and len(procurements) > 0

def load_contractor_registry():
    global contractor_registry
    json_result = []
    with open('contractor_registry.json', 'r') as f:
        json_result = json.load(f)

    result = {}
    for registry in json_result:
        result[registry["workhead"]] = registry
    contractor_registry = result
    print contractor_registry

