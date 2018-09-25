import data_holder
"""
Returns list of registered contractors that are awarded 
"""
def get_registered_contractors():
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
            registered_contractors.add(contractor)

    return registered_contractors


def function_4():
    result = []
    result.append('Registered contractors:')

    contractor_names = map(lambda c: c.company_name, get_registered_contractors())
    result.extend(contractor_names)

    return '\n'.join(result)