import data_holder

amt_awarded_to_reg = .0
amt_awarded_to_unreg = .0
top5_contractors_and_amount = []


def is_initialized():
    return len(top5_contractors_and_amount) > 0


def init_data():
    if is_initialized():
        return

    global amt_awarded_to_reg
    global amt_awarded_to_unreg
    global top5_contractors_and_amount

    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
    company_awarded_amt_dict = {}

    for procurement in data_holder.procurements:
        if not procurement.awarded:
            continue

        if procurement.supplier_name in contractor_dict:
            company_awarded_amt_dict.setdefault(procurement.supplier_name, 0)
            company_awarded_amt_dict[procurement.supplier_name] += procurement.awarded_amt
            amt_awarded_to_reg += procurement.awarded_amt
        else:
            amt_awarded_to_unreg += procurement.awarded_amt

    sorted_company_names = sorted(company_awarded_amt_dict.keys(),
                                  key=company_awarded_amt_dict.get,
                                  reverse=True)  # sort keys in descending order based on value of a given key
    # create a list of tuples containing (company_name, total procurement amount)
    top5_contractors_and_amount = map(lambda c: (c, company_awarded_amt_dict[c]), sorted_company_names[:5])


def top_contractors_and_amount():
    init_data()
    return top5_contractors_and_amount


def amount_awarded_to_registered_contractors():
    init_data()
    return amt_awarded_to_reg


def amount_awarded_to_unregistered_contractors():
    init_data()
    return amt_awarded_to_unreg


def function_5():
    result = []
    result.append('====')
    result.append('Top 5 companies with the most tenders:')

    top_5_company_name_and_amt = map(lambda company_and_amount: '%s with awarded amount %f' % company_and_amount,
                                     top_contractors_and_amount())
    result.extend(top_5_company_name_and_amt)

    result.append('====')
    result.append('Amount awarded to registered contractors: %f' % amount_awarded_to_registered_contractors())
    result.append('====')
    result.append('Amount awarded unregistered contractors: %f' % amount_awarded_to_unregistered_contractors())

    return '\n'.join(result)
