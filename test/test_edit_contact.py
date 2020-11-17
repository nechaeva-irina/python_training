# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Oleg", middlename="Olegovich", lastname="Ivanov", nickname="IVO",
                                   title="Testing", company_name="TestCompany",
                                   company_address="Moscow, Sovetskaya str.138",
                                   homephone="777-62-48", mobilephone="947-242-952", workphone="826-42-67",
                                   fax="927-42-64",
                                   email1="test@test.com", email2="test2@test.com", email3="test3@test.com",
                                   homepage="www.training.com", bday="12", bmonth="June", byear="1983",
                                   aday="16", amonth="September", address2="Sovetskaya,138", homephone2="535-25-63"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="Peter", title="CEO",
                      company_name="SunnyComp", company_address="Warsaw, Novaya str.54-87",
                      homephone="938-524-632", mobilephone="952-7777-33", workphone="6244-786-3222", fax="93-52-67",
                      email1="new@test.com", email2="new2@test.com", email3="new3@test.com",
                      homepage="www.sunny.com", bday="3", bmonth="December", byear="1996",
                      aday="28", amonth="March", address2="Staraya,6", homephone2="111-55-3333")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index,contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
