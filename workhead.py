"""
This module holds the Workhead class that models after the workhead of contractors in the excel sheet
It also holds definitions for workhead grades and categories
"""

import data_holder

WORKHEAD_CATEGORIES = {
    "CW": "Construction",
    "CR": "Construction-Related",
    "ME": "Mechanical and Electrical",
    "MW": "Maintenance",
    "TR": "Trade Heads for sub-contractors",
    "RW": "Regulatory Workhead",
    "SY": "Supply"
}

# tendering limits -1 means unlimited
# The unit is millions
CONSTRUCTION_GRADE_TENDERING_LIMITS = {
    "A1": -1,
    "A2": 85,
    "B1": 40,
    "B2": 13,
    "C1": 4,
    "C2": 1.3,
    "C3": 0.65
}

SPECIALISTS_GRADE_TENDERING_LIMIT = {
    "Single Grade": -1,
    "L6": -1,
    "L5": 13,
    "L4": 6.5,
    "L3": 4,
    "L2": 1.3,
    "L1": 0.65
}


class Workhead:
    """
    A class that models after the workhead of contractors in the excel sheet
    """
    _contractors = []
    _procurements = []

    def __init__(self, workhead, grade, expiry_date):
        self.workhead = workhead
        self.grade = grade
        self.expiry_date = expiry_date
        self.category_abbreviation = self.workhead[0:2]

    def workhead_category_title(self):
        """
        Tells the title of the category the workhead is in
        :return: String
        """
        return WORKHEAD_CATEGORIES[self.category_abbreviation]

    # according to https://www.bca.gov.sg/ContractorsRegistry/contractors_tendering_limits.html
    def tendering_limit(self):
        limit = -1
        if self.category_abbreviation == "CW":
            limit = CONSTRUCTION_GRADE_TENDERING_LIMITS[self.grade]
        elif self.category_abbreviation in ["CR", "ME", "MW", "SY"]:
            limit = SPECIALISTS_GRADE_TENDERING_LIMIT[self.grade]

        if limit == -1:
            return 'Unlimited'
        else:
            return '%.1f Million' % limit

    def display_text(self):
        """
        String representation of the workhead instance
        :return: String
        """
        result = [workhead_display_text(self.workhead)]
        result.append("\tExpiry Date:")
        result.append("\t%s" % self.expiry_date)
        result.append('\tTendering Limit:')
        result.append('\t%s' % self.tendering_limit())

        return '\n'.join(result)


def workhead_display_text(workhead):
    """
    Tells Title, description of the given workhead
    :param workhead: Workhead of contractor
    :return: String
    """
    result = []
    workhead_info = data_holder.contractor_registry[workhead]
    result.append('\tWorkhead Code:')
    result.append("\t%s" % workhead)
    result.append('\tTitle:')
    result.append("\t%s" % workhead_info["title"])
    result.append('\tDescription:')
    result.append("\t%s" % workhead_info["description"])

    return '\n'.join(result)