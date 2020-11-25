# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middletname", 15),
            lastname=random_string("lastname", 20), nickname=random_string("nicktname", 10),
            title="Testing", company_name="TestCompany",
            company_address="Moscow, Sovetskaya str.138",
            homephone="777-62-48", mobilephone="947-242-952", workphone="826-42-67", fax="927-42-64",
            email1="test@test.com", email2="test2@test.com", email3="test3@test.com",
            homepage="www.training.com", bday="12", bmonth="June", byear="1983",
            aday="16", amonth="September", address2="Sovetskaya,138", homephone2="535-25-63")
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
