from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    random_group_to_edit = random.choice(old_groups)
    updated_group_info = Group(name="New name")
    app.group.edit_group_by_id(random_group_to_edit.id, updated_group_info)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_group_header(app):
#    if app.group.count() == 0:
#       app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#   app.group.edit_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)
