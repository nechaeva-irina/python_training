# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IVO",
                               title="Testing", company_name="TestCompany",
                               company_address="Moscow, Sovetskaya str.138",
                               homephone="777-62-48", mobilephone="947-242-952", workphone="826-42-67", fax="927-42-64",
                               email1="test@test.com", email2="test2@test.com", email3="test3@test.com",
                               homepage="www.training.com", bday="12", bmonth="June", byear="1983",
                               aday="16", amonth="September", address2="Sovetskaya,138", homephone2="535-25-63"))
    app.session.logout()
