"""
The modules contains the Procurement and Contractor class
"""
from workhead import *


class Contractor:
    """
    A class that models the given data in the contractor excel sheet

    Automatically processed columns:
    company_name
    uen_no
    building_no
    street_name
    unit_no
    building_name
    postal_code
    tel_no

    Manually handled columns:
    workhead
    grade
    expiry_date

    Other attibutes:
    workheads

    Workheads is accessible via the workheads attribute of an instance of this class
    """
    AUTO_ATTRIBUTES = ["company_name", "uen_no", "additional_info", "building_no",
                       "street_name", "unit_no", "building_name", "postal_code", "tel_no"]

    def __init__(self, contractor_sequence):
        self.tel_no = None
        self.postal_code = None
        self.building_name = None
        self.unit_no = None
        self.street_name = None
        self.building_no = None
        self.uen_no = None
        self.additional_info = None
        self.company_name = None

        self.workheads = set()
        self.add_workhead(contractor_sequence['workhead'], contractor_sequence['grade'],
                          contractor_sequence['expiry_date'])

        for attr in self.AUTO_ATTRIBUTES:
            setattr(self, attr, contractor_sequence[attr])

    def add_workhead(self, wh, grade, expiry_date):
        """
        Adds workhead to contractor

        :param wh: workhead
        :param grade: grade of workhead
        :param expiry_date: expiry date of workhead
        :return: None
        """
        workhead = Workhead(wh, grade, expiry_date)
        self.workheads.add(workhead)

    def is_in_workhead_category(self, workhead_category):
        """
        Tells if contractor is part of the given workhead category
        :param workhead_category: Workhead category
        :return: True or False
        """
        for workhead in self.workheads:
            if workhead.category_abbreviation == workhead_category:
                return True
        return False

    def is_in_workhead(self, workhead):
        """
        Tells if contractor has a given workhead
        :param workhead:
        :return: True or False
        """
        for wh in self.workheads:
            if wh.workhead == workhead:
                return True
        return False

    def display_text(self):
        """
        Provide a string representing the contractor instance
        :return: String
        """
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


class Procurement:
    """
    attributes:

    Automatic Attributes:
    tender_no
    agency
    tender_description
    award_date
    tender_detail_status
    supplier_name
    awarded_amt

    Other attributes:
    awarded
    """
    AUTO_ATTRIBUTES = ["tender_no", "agency", "tender_description",
                  "award_date", "tender_detail_status", "supplier_name",
                  "awarded_amt"]

    def __init__(self, contractor_sequence):
        self.tender_no = None
        self.agency = None
        self.tender_description = None
        self.award_date = None
        self.tender_detail_status = None
        self.supplier_name = None
        self.awarded_amt = 0

        for i in range(len(self.AUTO_ATTRIBUTES)):
            attribute_name = self.AUTO_ATTRIBUTES[i]
            setattr(self, attribute_name, contractor_sequence[i])

        self.awarded_amt = float(self.awarded_amt)

        if self.awarded_amt > 0:
            self.awarded = True
        else:
            self.awarded = False
            self.supplier_name = None

    def display_text(self):
        """
        Provide a string representing the procurement instance
        :return: String
        """
        lines = []
        for attr in self.AUTO_ATTRIBUTES:
            lines.append('%s: %s' % (attr, str(getattr(self, attr))))

        return '\n'.join(lines)
