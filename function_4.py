import data_holder
"""
Returns list of registered contractors that are awarded 
"""




def get_registered_contractors_supplier():
    # at this point the cache is not yet set
    # so we initialize it
    registered_contractors = set()
    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
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
    # at this point the cache is not yet set
    # so we initialize it
    registered_contractors = set()
    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
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
    result = []
    result.append('Registered contractors with supplier:')

    result2 = []
    result2.append('\n' + '\n'+ '\n'+ 'Registered contractors with items:')

    contractor_names = map(lambda c: c.company_name, get_registered_contractors_supplier())
    result.extend(contractor_names)

    contractor_names2 = map(lambda c: c.company_name, get_registered_contractors_items())
    result2.extend(contractor_names2)

    return '\n'.join(result + result2)
