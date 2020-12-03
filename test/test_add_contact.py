# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middletname", 15),
            lastname=random_string("lastname", 20), nickname=random_string("nicktname", 10),
            title=random_string("title", 15), company_name=random_string("company_name", 15),
            company_address=random_string("company_address", 20),
            homephone=random_string("H", 9), mobilephone=random_string("M", 9), workphone=random_string("W", 9),
            fax=random_string("F", 9), email1=random_string("E1", 10), email2=random_string("E2", 10),
            email3=random_string("E3", 10), homepage=random_string("HP", 10), bday="12", bmonth="June",
            byear=random_string("", 4), aday="16", amonth="September", address2=random_string("address2", 15),
            homephone2=random_string("H", 9))
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
