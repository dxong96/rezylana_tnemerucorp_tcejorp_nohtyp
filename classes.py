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
    ATTRIBUTES = ["company_name", "uen_no", "workhead", "grade", \
                  "additional_info", "expiry_date", "building_no", \
                  "street_name", "unit_no", "building_name", "postal_code",\
                  "tel_no"]
    def __init__(self, contractor_sequence):
        for i in range(len(self.ATTRIBUTES)):
            attribute_name = self.ATTRIBUTES[i]
            setattr(self, attribute_name, contractor_sequence[i])


CONTRACTORS_CSV_PATH = "C:\Users\Dx\Documents\SIT\ICT 1002 Programming Fundamentals\Python Project\Project Datasets\listing-of-registered-contractors\listing-of-registered-contractors.csv"
PROCUREMENTS_CSV_PATH = "C:\Users\Dx\Documents\SIT\ICT 1002 Programming Fundamentals\Python Project\Project Datasets\government-procurement\government-procurement-via-gebiz.csv"
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
    ATTRIBUTES = ["tender_no", "agency", "tender_description", \
                  "award_date", "tender_detail_status", "supplier_name",\
                  "awarded_amt"]
    def __init__(self, contractor_sequence):
        for i in range(len(self.ATTRIBUTES)):
            attribute_name = self.ATTRIBUTES[i]
            setattr(self, attribute_name, contractor_sequence[i])

        if self.tender_detail_status == "Awarded to Suppliers":
            self.awarded = True
        else:
            self.awarded = False
            self.supplier_name = None
