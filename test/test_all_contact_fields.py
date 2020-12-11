import re
from model.contact import Contact


def test_all_contacts_fields_on_main_page(app, db):
    list_of_contacts = db.get_contact_list()
    assert len(list_of_contacts) == app.contact.count()
    for i in range(len(list_of_contacts)):
        contact_from_home_page_by_index = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[i]
        contact_from_db_by_index = db.get_contact_list()[i]
        assert contact_from_home_page_by_index.lastname == contact_from_db_by_index.lastname
        assert contact_from_home_page_by_index.firstname == contact_from_db_by_index.firstname
        assert contact_from_home_page_by_index.company_address == contact_from_db_by_index.company_address
        assert contact_from_home_page_by_index.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db_by_index)
        assert contact_from_home_page_by_index.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db_by_index)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.homephone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))
