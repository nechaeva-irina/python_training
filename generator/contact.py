# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.dumps(testdata, indent=2))
