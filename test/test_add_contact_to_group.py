import random
from model.group import Group
from model.contact import Contact


def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Oleg", middlename="Olegovich", lastname="Ivanov", nickname="IVO",
                                   title="Testing", company_name="TestCompany",
                                   company_address="Moscow, Sovetskaya str.138",
                                   homephone="777-62-48", mobilephone="947-242-952", workphone="826-42-67",
                                   fax="927-42-64",
                                   email1="test@test.com", email2="test2@test.com", email3="test3@test.com",
                                   homepage="www.training.com", bday="12", bmonth="June", byear="1983",
                                   aday="16", amonth="September", address2="Sovetskaya,138", homephone2="535-25-63"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    list_of_groups = db.get_group_list()
    group_to_add = random.choice(list_of_groups)
    list_of_contacts = db.get_contact_list()
    contact_to_add = random.choice(list_of_contacts)
    app.contact.add_contact_to_group(contact_to_add.id, group_to_add.id)
    list_of_contacts_new = db.get_contact_list()
    assert len(list_of_contacts) == len(list_of_contacts_new)
    if check_ui:
        assert sorted(list_of_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
