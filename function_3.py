import data_holder


def list_of_agency_and_awarded_amount(asc):
    # create a dictionary with key, agency name, and value, list of procurement object
    agency_to_procurements = data_holder.create_dict_for_list(data_holder.procurements, 'agency')

    agency_to_awarded_amt = {}
    # convert the list of procurement to awarded amount
    for agency in agency_to_procurements:
        agency_to_awarded_amt.setdefault(agency, 0)
        for p in agency_to_procurements[agency]:
            agency_to_awarded_amt[agency] += p.awarded_amt

    sorted_keys = sorted(agency_to_procurements.keys(), key=agency_to_procurements.get, reverse=not asc)
    # return result as a list of tuples (agency name, total amount awarded for this agency)
    return [(key, agency_to_awarded_amt[key]) for key in sorted_keys]


def function_3(asc):
    result = list_of_agency_and_awarded_amount(asc)
    return '\n'.join(['%s, total amount awarded: %.2f' % item for item in result])
