class PersonalInfo:
    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname


class CompanyInfo:
    def __init__(self, title, company_name, company_address):
        self.title = title
        self.company_name = company_name
        self.company_address = company_address


class Phones:
    def __init__(self, homephone, mobilephone, workphone, fax):
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax


class Emails:
    def __init__(self, email1, email2, email3):
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3


class Homepage:
    def __init__(self, homepage):
        self.homepage = homepage


class ImportantDates:
    def __init__(self, bday, bmonth, byear, aday, amonth):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth


class OtherInfo:
    def __init__(self, address2, homephone):
        self.address2 = address2
        self.homephone = homephone
