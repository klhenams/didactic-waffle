from django.test import RequestFactory

from django_crud.addressbooks.models import Contact, Email, Group, PhoneNumber
from django_crud.addressbooks.views import (
    ContactViewSet,
    EmailContactViewSet,
    GroupViewSet,
    PhoneContactViewSet,
)


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


class TestEmailContactViewSet:
    def test_email_contact_get_queryset(self, email_contact: Email, rf: RequestFactory):
        view = EmailContactViewSet()
        request = rf.get("/fake-url/")
        request.user = email_contact.contact.group.user

        view.request = request

        assert email_contact in view.get_queryset()

    def test_create_email_contact(self, contact, rf: RequestFactory):
        view = EmailContactViewSet()
        data = {
            "contact": contact.pk,
            "email": "janedoe@example.co",
        }
        request = rf.post("/fake-url/")
        request.user = contact.group.user
        request.data = data

        view.request = request
        view.format_kwarg = "json"
        response = view.create(request)

        assert response.data["email"] == data["email"]


class TestPhoneContactViewSet:
    view = PhoneContactViewSet()

    def test_phone_contact_get_queryset(
        self, phonenumber_contact: PhoneNumber, rf: RequestFactory
    ):
        request = rf.get("/fake-url/")
        request.user = phonenumber_contact.contact.group.user

        self.view.request = request

        assert phonenumber_contact in self.view.get_queryset()

    def test_create_phone_contact(self, contact, rf: RequestFactory):
        data = {
            "contact": contact.pk,
            "phone_number": "+233200105693",
        }
        request = rf.post("/fake-url/")
        request.user = contact.group.user
        request.data = data

        self.view.request = request
        self.view.format_kwarg = "json"
        response = self.view.create(request)

        assert response.data["phone_number"] == data["phone_number"]
