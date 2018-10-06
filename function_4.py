import data_holder
import sys
"""
Returns list of registered contractors that are awarded 
"""




def get_registered_contractors_supplier():
    '''Get the list of contractors that is awarded to supplier'''
    # at this point the cache is not yet set
    # so we initialize it
    registered_contractors = set()
    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
    #loop through the csv file and check which contractor is a registered vendor and is awarded to suppliers
    for procurement in data_holder.procurements:
        if not procurement.awarded:
            continue

        if procurement.supplier_name not in contractor_dict:
            continue

        for contractor in contractor_dict[procurement.supplier_name]:
            if procurement.tender_detail_status == "Awarded to Suppliers":
                registered_contractors.add(contractor)

    return registered_contractors


def get_registered_contractors_items():
    '''Get the list of contractors that is awarded by items'''
    # at this point the cache is not yet set
    # so we initialize it
    registered_contractors = set()
    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
    # loop through the csv file and check which contractor is a registered vendor and is awarded by items
    for procurement in data_holder.procurements:
        if not procurement.awarded:
            continue

        if procurement.supplier_name not in contractor_dict:
            continue

        for contractor in contractor_dict[procurement.supplier_name]:
            if procurement.tender_detail_status == "Awarded by Items":
                registered_contractors.add(contractor)

    return registered_contractors

def function_4():
    ''' append the list of registered vendor awarded and awarded by items and return the result '''
    supplierResult = []
    supplierResult.append('Awarded Registered contractors:' + '\n')

    itemResult = []
    itemResult.append('\n'+ '\n'+ 'Registered contractors awarded with items:' + '\n')

    awarded_names = map(lambda c: c.company_name, get_registered_contractors_supplier())
    supplierResult.extend(awarded_names)
    sortSupplier = supplierResult[:1] + sorted(supplierResult[1:])

    awardeditems_names = map(lambda c: c.company_name, get_registered_contractors_items())
    itemResult.extend(awardeditems_names)
    sortItem = itemResult[:1] + sorted(itemResult[1:])
    return '\n'.join(sortSupplier+ sortItem)

