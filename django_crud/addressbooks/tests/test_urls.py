from django.urls import resolve, reverse

from django_crud.addressbooks.models import Group


def test_addressbook_group_detail(group: Group):
    assert (
        reverse("app:group-detail", kwargs={"pk": group.pk})
        == f"/app/address/groups/{group.pk}/"
    )
    assert resolve(f"/app/address/groups/{group.pk}/").view_name == "app:group-detail"


def test_addressbook_group_list():
    assert reverse("app:group-list") == "/app/address/groups/"
    assert resolve("/app/address/groups/").view_name == "app:group-list"
