import random
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture


def test_delete_contact_from_group(app, db, check_ui):
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
    old_contacts = db.get_contact_list()
    contact_to_delete = random.choice(old_contacts)
    list_of_groups = db.get_group_list()
    group_for_deletion = random.choice(list_of_groups)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    l = db.get_contacts_in_group(Group(id=group_for_deletion.id))
    if contact_to_delete not in l:
        app.contact.add_contact_to_group(contact_to_delete.id, group_for_deletion.id)
    app.contact.delete_contact_from_group(contact_to_delete.id, group_for_deletion.id)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
