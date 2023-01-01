from django.test import RequestFactory

from django_crud.addressbooks.models import Contact, Group
from django_crud.addressbooks.views import ContactViewSet, GroupViewSet


class TestGroupViewSet:
    def test_get_queryset(self, group: Group, rf: RequestFactory):
        view = GroupViewSet()
        request = rf.get("/fake-url/")
        request.user = group.user

        view.request = request

        assert group in view.get_queryset()

    def test_create_group(self, user, rf: RequestFactory):
        view = GroupViewSet()
        group = "Group 4"
        request = rf.post("/fake-url/")
        request.user = user
        request.data = {"name": group}

        view.request = request
        view.format_kwarg = "json"
        response = view.create(request)

        assert response.data["name"] == group

    def test_update_group(self, user, group: Group, rf: RequestFactory):
        view = GroupViewSet()
        edited_group = "Group Modify"
        request = rf.put("/fake-url/")
        request.user = user
        request.data = {"name": edited_group}

        view.request = request
        view.format_kwarg = "json"
        response = view.create(request)

        assert response.data["name"] == edited_group


class TestContactViewSet:
    def test_contact_get_queryset(self, contact: Contact, rf: RequestFactory):
        view = ContactViewSet()
        request = rf.get("/fake-url/")
        request.user = contact.group.user

        view.request = request

        assert contact in view.get_queryset()

    def test_create_contact(self, group, rf: RequestFactory):
        view = ContactViewSet()
        data = {
            "group": group.pk,
            "name": "Ama Tutum",
            "email_set": ["nksf@kldfj.co"],
            "phonenumber_set": ["+233270135690"],
        }
        request = rf.post("/fake-url/")
        request.user = group.user
        request.data = data

        view.request = request
        view.format_kwarg = "json"
        response = view.create(request)

        assert response.data["name"] == data["name"]
