import pytest

from django_crud.addressbooks.models import Group

from .factories import GroupFactory


@pytest.fixture
def group(db) -> Group:
    return GroupFactory()
