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

    def __init__(self, workhead, grade):
        self.workhead = workhead
        self.grade = grade
        self.category_abbreviation = self.workhead[0:2]

    def workhead_title(self):
        return WORKHEAD_CATEGORIES[self.category_abbreviation]

    # according to https://www.bca.gov.sg/ContractorsRegistry/contractors_tendering_limits.html
    def tendering_limit(self):
        if self.category_abbreviation == "CW":
            return CONSTRUCTION_GRADE_TENDERING_LIMITS[self.category_abbreviation]
        elif self.category_abbreviation in ["CR", "ME", "MW", "SY"]:
            return SPECIALISTS_GRADE_TENDERING_LIMIT[self.category_abbreviation]
        else:
            return -1



def get_contractors_by_industry_abbreviation(industry_abbreviation):
    contractors = []
    for c in data_holder.contractors:
        if c.is_in_industry(industry_abbreviation):
            contractors.append(c)

    return contractors