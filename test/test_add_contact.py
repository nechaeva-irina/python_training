# -*- coding: utf-8 -*-
from fixture.application2 import Application2
import pytest


@pytest.fixture()
def app2(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy2)
    return fixture


def test_add_contact(app2):
    app2.session.login(username="admin", password="secret")
    app2.contact.create()
    app2.session.logout()