from django.urls import resolve, reverse

from django_crud.addressbooks.models import Contact, Group


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
