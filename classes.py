import data_holder
from workhead import *


"""
Contractor attributes:

company_name
uen_no
workhead
grade
additional_info
expiry_date
building_no
street_name
unit_no
building_name
postal_code
tel_no
"""
class Contractor:
    AUTO_ATTRIBUTES = ["company_name", "uen_no", "additional_info", "expiry_date", "building_no",
                       "street_name", "unit_no", "building_name", "postal_code", "tel_no"]

    def __init__(self, contractor_sequence):
        self.workheads = set()
        self.add_workhead(contractor_sequence['workhead'], contractor_sequence['grade'])

        for attr in self.AUTO_ATTRIBUTES:
            setattr(self, attr, contractor_sequence[attr])

    def add_workhead(self, workhead, grade):
        industry = Workhead(workhead, grade)
        self.workheads.add(industry)

    def is_in_industry(self, industry_abbreviation):
        for industry in self.workheads:
            if industry.industry_abbreviation == industry_abbreviation:
                return True
        return False



"""
Procurement attributes:

tender_no.
agency
tender_description
award_date
tender_detail_status
supplier_name
awarded_amt
"""
class Procurement:
    ATTRIBUTES = ["tender_no", "agency", "tender_description",
                  "award_date", "tender_detail_status", "supplier_name",
                  "awarded_amt"]

    def __init__(self, contractor_sequence):
        for i in range(len(self.ATTRIBUTES)):
            attribute_name = self.ATTRIBUTES[i]
            setattr(self, attribute_name, contractor_sequence[i])

        if self.awarded_amt > 0:
            self.awarded = True
        else:
            self.awarded = False
            self.supplier_name = None

        self.awarded_amt = float(self.awarded_amt)
