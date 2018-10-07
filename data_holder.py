"""
This modules contains the procurements and contractors loaded from the excel sheets.
It also provides methods to fetch specific data based on the loaded procurements and contractors
"""

import csv
import json
from classes import Contractor
from classes import Procurement

contractors = []
procurements = []
contractor_registry = {}
contractors_source_path = None
procurements_source_path = None


def load_contractor_list(path):
    """
    Load the excel sheet at the given path into module variable contractors
    :param path: Path of the contractors excel sheet
    :return: None
    """
    global contractors_source_path
    contractors_source_path = path
    contractor_dict = {}
    with open(path, 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            company_name = row['company_name']
            if company_name in contractor_dict:
                contractor = contractor_dict[company_name]
                contractor.add_workhead(row['workhead'], row['grade'], row['expiry_date'])
            else:
                contractor = Contractor(row)
                contractor_dict[company_name] = contractor

        f.close()

    global contractors  # we need to write global to be able to assign to the module variables
    contractors = contractor_dict.values()


def load_procurement_list(path):
    """
    Load the excel sheet at the given path into module variable procurements
    :param path: Path of procurement excel sheet
    :return: None
    """
    global procurements_source_path
    procurements_source_path = path
    new_procurements = []
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        reader.next()  # read the next row therefore skipping the first row
        for row in reader:
            # check line for commas to ensure
            procurement = Procurement(row)
            new_procurements.append(procurement)
        f.close()

    global procurements
    procurements = new_procurements


def create_dict_for_list(items, key):
    """
    A helper method that groups an object based on its attribute
    :param items: The list of objects
    :param key: The key to group
    :return: A dictionary of that maps value of the given key to a list of the object
    """
    result = {}
    for item in items:
        result.setdefault(getattr(item, key), [])
        result[getattr(item, key)].append(item)
    return result


def are_sheets_loaded():
    """
    Check if both contractors and procurements are already loaded into the application
    :return: True or False
    """
    return len(contractors) > 0 and len(procurements) > 0


def load_contractor_registry():
    """
    Loads extra information on the every workhead into module variable contractor_registry
    :return: None
    """
    global contractor_registry
    json_result = []
    with open('contractor_registry.json', 'r') as f:
        json_result = json.load(f)

    result = {}
    for registry in json_result:
        result[registry["workhead"]] = registry
    contractor_registry = result


def get_contractors_by_workhead(workhead):
    """
    Filter the contractors down to those that have the given workhead
    :param workhead: The workhead to filter by
    :return: A list of contractor
    """
    result = []
    global contractors
    for c in contractors:
        if c.is_in_workhead(workhead):
            result.append(c)

    return result


def get_workheads_for_category(workhead_category):
    """
    Filter the contractors by the workhead category
    :param workhead_category: Workhead category, Example (TR, CR)
    :return: A list of contractors
    """
    result = []
    global contractor_registry
    for workhead in contractor_registry:
        wh_category = workhead[0:2]
        if wh_category == workhead_category:
            result.append(workhead)

    return result
