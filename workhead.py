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
    _contractors = []
    _procurements = []

    def __init__(self, workhead, grade, expiry_date):
        self.workhead = workhead
        self.grade = grade
        self.expiry_date = expiry_date
        self.category_abbreviation = self.workhead[0:2]

    def workhead_category_title(self):
        return WORKHEAD_CATEGORIES[self.category_abbreviation]

    # according to https://www.bca.gov.sg/ContractorsRegistry/contractors_tendering_limits.html
    def tendering_limit(self):
        if self.category_abbreviation == "CW":
            return CONSTRUCTION_GRADE_TENDERING_LIMITS[self.category_abbreviation]
        elif self.category_abbreviation in ["CR", "ME", "MW", "SY"]:
            return SPECIALISTS_GRADE_TENDERING_LIMIT[self.category_abbreviation]
        else:
            return -1


    def display_text(self):
        result = [workhead_display_text(self.workhead)]
        result.append("Expiry Date:")
        result.append("\t%s" % self.expiry_date)

        return '\n'.join(result)


def workhead_display_text(workhead):
    result = []
    workhead_info = data_holder.contractor_registry[workhead]
    result.append('\tWorkhead Code:')
    result.append("\t%s" % workhead)
    result.append('\tTitle:')
    result.append("\t%s" % workhead_info["title"])
    result.append('\tDescription:')
    result.append("\t%s" % workhead_info["description"])

    return '\n'.join(result)