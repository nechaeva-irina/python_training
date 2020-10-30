# -*- coding: utf-8 -*-
from application2 import Application2
import pytest


@pytest.fixture()
def app2(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy2)
    return fixture


def test_add_contact(app2):
    app2.login(username="admin", password="secret")
    app2.create_contact()
    app2.logout()