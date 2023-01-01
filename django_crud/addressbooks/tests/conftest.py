import pytest

from django_crud.addressbooks.models import Contact, Email, Group, PhoneNumber

from .factories import (
    ContactFactory,
    EmailContactFactory,
    GroupFactory,
    PhoneNumberContactFactory,
)


@pytest.fixture
def group(db) -> Group:
    return GroupFactory()


@pytest.fixture
def contact(db) -> Contact:
    return ContactFactory()


@pytest.fixture
def email_contact(db) -> Email:
    return EmailContactFactory()


@pytest.fixture
def phonenumber_contact(db) -> PhoneNumber:
    return PhoneNumberContactFactory()
