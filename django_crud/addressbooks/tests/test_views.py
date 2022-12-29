from django.test import RequestFactory

from django_crud.addressbooks.models import Group
from django_crud.addressbooks.views import GroupViewSet


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
