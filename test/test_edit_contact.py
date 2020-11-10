# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(
        Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="Peter", title="CEO",
                company_name="SunnyComp", company_address="Warsaw, Novaya str.54-87",
                homephone="938-524-632", mobilephone="952-7777-33", workphone="6244-786-3222", fax="93-52-67",
                email1="new@test.com", email2="new2@test.com", email3="new3@test.com",
                homepage="www.sunny.com", bday="3", bmonth="December", byear="1996",
                aday="28", amonth="March", address2="Staraya,6", homephone2="111-55-3333"))
