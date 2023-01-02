from django.urls import resolve, reverse

from django_crud.addressbooks.models import Contact, Email, Group


def test_addressbook_group_detail(group: Group):
    assert (
        reverse("app:group-detail", kwargs={"pk": group.pk})
        == f"/app/address/groups/{group.pk}/"
    )
    assert resolve(f"/app/address/groups/{group.pk}/").view_name == "app:group-detail"


def test_addressbook_group_list():
    assert reverse("app:group-list") == "/app/address/groups/"
    assert resolve("/app/address/groups/").view_name == "app:group-list"


def test_addressbook_contact_detail(contact: Contact):
    assert (
        reverse("app:contact-detail", kwargs={"pk": contact.pk})
        == f"/app/address/contacts/{contact.pk}/"
    )
    assert (
        resolve(f"/app/address/contacts/{contact.pk}/").view_name
        == "app:contact-detail"
    )


def test_addressbook_contact_list():
    assert reverse("app:contact-list") == "/app/address/contacts/"
    assert resolve("/app/address/contacts/").view_name == "app:contact-list"


def test_addressbook_email_contact_detail(email_contact: Email):
    assert (
        reverse("app:email-detail", kwargs={"pk": email_contact.pk})
        == f"/app/address/emails/{email_contact.pk}/"
    )
    assert (
        resolve(f"/app/address/emails/{email_contact.pk}/").view_name
        == "app:email-detail"
    )


def test_addressbook_email_contact_list():
    assert reverse("app:email-list") == "/app/address/emails/"
    assert resolve("/app/address/emails/").view_name == "app:email-list"


def test_addressbook_email_contact_related_list(contact: Contact):
    assert (
        reverse("app:email-contact", kwargs={"pk": contact.pk})
        == f"/app/address/emails/{contact.pk}/contact/"
    )
    assert (
        resolve(f"/app/address/emails/{contact.pk}/contact/").view_name
        == "app:email-contact"
    )
