import data_holder

"""
shows a company's grade. ( still creating or attempting to let it sort)
"""

def get_contractors_by_workhead(workhead):
    contractors = []
    for c in data_holder.contractors:
        if c.is_in_workhead(workhead):
            contractors.append(c)

    return contractors


def get_workheads_for_category(workhead_category):
    result = []
    for workhead in data_holder.contractor_registry:
        wh_category = workhead[0:2]
        if wh_category == workhead_category:
            result.append(workhead)

    return result