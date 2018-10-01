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
    AUTO_ATTRIBUTES = ["company_name", "uen_no", "additional_info", "building_no",
                       "street_name", "unit_no", "building_name", "postal_code", "tel_no"]

    def __init__(self, contractor_sequence):
        self.workheads = set()
        self.add_workhead(contractor_sequence['workhead'], contractor_sequence['grade'], contractor_sequence['expiry_date'])

        for attr in self.AUTO_ATTRIBUTES:
            setattr(self, attr, contractor_sequence[attr])

    def add_workhead(self, wh, grade, expiry_date):
        workhead = Workhead(wh, grade, expiry_date)
        self.workheads.add(workhead)

    def is_in_workhead_category(self, category_abbreviation):
        for workhead in self.workheads:
            if workhead.category_abbreviation == category_abbreviation:
                return True
        return False

    def is_in_workhead(self, workhead):
        for wh in self.workheads:
            if wh.workhead == workhead:
                return True
        return False

    def display_text(self):
        result = ["Company name:"]
        result.append(self.company_name)
        result.append("Uen No:")
        result.append(self.uen_no)
        result.append("Additional Information:")
        result.append(self.additional_info)
        result.append("Address:")
        result.append(self.building_no)
        result.append(self.street_name)

        if self.unit_no != 'na':
            result.append(self.unit_no)

        if self.building_name != 'na':
            result.append(self.building_name)
        result.append('S(%s)' % self.postal_code)
        result.append('Contact No:')
        result.append(self.tel_no)

        result.append('Workheads:')
        result.extend(map(lambda w: w.display_text(), self.workheads))

        return '\n'.join(result)




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
