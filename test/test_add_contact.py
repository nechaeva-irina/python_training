# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IVO",
                      title="Testing", company_name="TestCompany",
                      company_address="Moscow, Sovetskaya str.138",
                      homephone="777-62-48", mobilephone="947-242-952", workphone="826-42-67", fax="927-42-64",
                      email1="test@test.com", email2="test2@test.com", email3="test3@test.com",
                      homepage="www.training.com", bday="12", bmonth="June", byear="1983",
                      aday="16", amonth="September", address2="Sovetskaya,138", homephone2="535-25-63")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
