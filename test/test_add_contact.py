# -*- coding: utf-8 -*-


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create()
    app.session.logout()