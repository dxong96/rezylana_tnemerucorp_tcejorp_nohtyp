"""
This modules contains a few functions that are used together to make function 5 possible
"""

import data_holder

_amt_awarded_to_reg = .0
_amt_awarded_to_unreg = .0
_top5_contractors_and_amount = []
_unreg_contractors_and_amount = []
_reg_contractors_and_amount = []


def is_initialized():
    """
    Tells if the module variables are set
    :return: Boolean
    """
    return len(_top5_contractors_and_amount) > 0


def init_data():
    """
    Contains the function 5 logic that sets the variables containing the result for caching
    :return: None
    """
    if is_initialized():  # checks if the result variables are already set
        return

    # result variables are not set
    global _amt_awarded_to_reg
    global _amt_awarded_to_unreg
    global _top5_contractors_and_amount
    global _reg_contractors_and_amount
    global _unreg_contractors_and_amount

    contractor_dict = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')
    company_awarded_amt_dict = {}
    reg_company_names = []
    unreg_company_names = []

    for procurement in data_holder.procurements:
        # skip not awarded procurement
        if not procurement.awarded:
            continue

        # group total procurements' awarded amount by company
        company_awarded_amt_dict.setdefault(procurement.supplier_name, 0)
        company_awarded_amt_dict[procurement.supplier_name] += procurement.awarded_amt

        # if supplier is registered
        if procurement.supplier_name in contractor_dict:
            _amt_awarded_to_reg += procurement.awarded_amt
            reg_company_names.append(procurement.supplier_name)
        else:
            _amt_awarded_to_unreg += procurement.awarded_amt
            unreg_company_names.append(procurement.supplier_name)

    # sorted the company names by total procurement amount
    sorted_company_names = sorted(company_awarded_amt_dict.keys(),
                                  key=company_awarded_amt_dict.get,
                                  reverse=True)
    # create a list of tuples containing (company_name, total procurement amount)
    _top5_contractors_and_amount = map(lambda c: (c, company_awarded_amt_dict[c]), sorted_company_names[:5])
    _reg_contractors_and_amount = map(lambda c: (c, company_awarded_amt_dict[c]), reg_company_names)
    _unreg_contractors_and_amount = map(lambda c: (c, company_awarded_amt_dict[c]), unreg_company_names)


def top_contractors_and_amount():
    """
    Initialize the result variables and return the top 5 company name and amount awarded
    :return: list of tuple containing the top 5 contractor company name and the amount awarded to them
    """
    init_data()
    return _top5_contractors_and_amount


def registered_contractors_and_amount():
    """
    Initialize the result variables and return registered company name and amount awarded
    :return: list of tuple containing registered company name and amount awarded
    """
    init_data()
    return _reg_contractors_and_amount


def unregistered_contractors_and_amount():
    """
    Initialize the result variables and return unregistered company name and amount awarded
    :return: list of tuple containing unregistered company name and amount awarded
    """
    init_data()
    return _unreg_contractors_and_amount


def amount_awarded_to_registered_contractors():
    """
    Initialize the result variables and return the total amounted awarded to registered contractors
    :return: Float
    """
    init_data()
    return _amt_awarded_to_reg


def amount_awarded_to_unregistered_contractors():
    """
    Initialize the result variables and return the total amounted awarded to unregistered contractors
    :return: Float
    """
    init_data()
    return _amt_awarded_to_unreg


def function_5():
    """
    String representation of all the outputs required of function 5
    :return: String
    """
    result = []
    result.append('Top 5 contractors with the most tenders:')

    top_5_company_name_and_amt = map(lambda company_and_amount: '%s with awarded amount $%.2f' % company_and_amount,
                                     top_contractors_and_amount())
    result.extend(top_5_company_name_and_amt)

    result.append('====')
    result.append('Total Amount awarded to registered contractors: $%.2f' % amount_awarded_to_registered_contractors())
    result.append('====')
    result.append('List of registered contractors and their awarded amount:')
    registered_company_name_and_amt = map(
        lambda company_and_amount: '%s with awarded amount $%.2f' % company_and_amount,
        registered_contractors_and_amount())
    result.extend(registered_company_name_and_amt)
    result.append('====')
    result.append('Total Amount awarded unregistered contractors: $%.2f' % amount_awarded_to_unregistered_contractors())
    result.append('====')
    result.append('List of unregistered contractors and their awarded amount:')
    unregistered_company_name_and_amt = map(
        lambda company_and_amount: '%s with awarded amount $%.2f' % company_and_amount,
        unregistered_contractors_and_amount())
    result.extend(unregistered_company_name_and_amt)

    return '\n'.join(result)
