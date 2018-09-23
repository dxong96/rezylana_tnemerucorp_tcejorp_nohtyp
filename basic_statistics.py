import data_holder

def generate_stats():
    """
    make a dict in the following format
    {
        company_name: contractor
    }
    """
    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
    procurement_list = data_holder.procurements
    procurement_count_dict = {}
    registered_contractors_names = set()
    unregistered_contractors_count = 0
    for procurement in procurement_list:
        if not procurement.awarded: # skip if it is not awarded to anyone
            continue
        if (procurement.supplier_name in contractor_dict): # a registered contractor
            registered_contractors_names.add(procurement.supplier_name)
        else: # a unregistered contractor
            unregistered_contractors_count += 0

        if (not procurement.supplier_name in procurement_count_dict): # when the dictionary do not have the company name as key
            procurement_count_dict[procurement.supplier_name] = 0 # we initialize it to zero so we can add on to it later
        procurement_count_dict[procurement.supplier_name] += 1

    sorted_company_names = sorted(procurement_count_dict.keys(), \
                                     key=procurement_count_dict.get, \
                                     reverse=True) # sort keys in descending order based on value of a given key
    top_5_company_names = sorted_company_names[:5]

    result = []
    result.append('Registered contractors:')

    result.extend(registered_contractors_names)
    result.append('====')
    result.append('Top 5 companies with the most tenders:')

    top_5_company_name_and_tenders = map(lambda name: \
            '%s with %d tenders' % (name, procurement_count_dict[name]), top_5_company_names)
    result.extend(top_5_company_name_and_tenders)

    result.append('====')
    result.append('Number of unregistered contractors: %d' \
                  % unregistered_contractors_count)
    result.append('====')
    result.append('Number of registered contractors: %d' \
                  % len(registered_contractors_names))

    return '\n'.join(result)
