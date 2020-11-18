from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_form()
        self.fill_personal_info(contact)
        self.fill_company_info(contact)
        self.fill_phones(contact)
        self.fill_emails(contact)
        self.fill_homepage(contact)
        self.fill_important_dates(contact)
        self.fill_other_info(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_new_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_personal_info(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_company_info(self, contact):
        wd = self.app.wd
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.company_address)

    def fill_phones(self, contact):
        wd = self.app.wd
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)

    def fill_emails(self, contact):
        wd = self.app.wd
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def fill_homepage(self, contact):
        wd = self.app.wd
        self.change_field_value("homepage", contact.homepage)

    def fill_important_dates(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)

    def fill_other_info(self, contact):
        wd = self.app.wd
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.homephone2)

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # init deletion
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # init edition
        ind2= index+1
        wd.find_element_by_xpath(f"/html/body/div/div[4]/form[2]/table/tbody/tr[{ind2}]/td[8]/a/img").click()
        # update contact info
        self.fill_personal_info(new_contact_data)
        self.fill_company_info(new_contact_data)
        self.fill_phones(new_contact_data)
        self.fill_emails(new_contact_data)
        self.fill_homepage(new_contact_data)
        self.fill_important_dates(new_contact_data)
        self.fill_other_info(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=text1, firstname=text2, id=id))
        return list(self.contact_cache)
