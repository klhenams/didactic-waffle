from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory

from django_crud.addressbooks.models import Contact, Email, Group, PhoneNumber
from django_crud.users.tests.factories import UserFactory


class GroupFactory(DjangoModelFactory):

    user = SubFactory(UserFactory)
    name = Sequence(lambda n: "Group %d" % n)

    class Meta:
        model = Group
        django_get_or_create = ["name"]


class ContactFactory(DjangoModelFactory):

    group = SubFactory(GroupFactory)
    name = Sequence(lambda n: "Contact %d" % n)

    class Meta:
        model = Contact
        django_get_or_create = ["name"]


class EmailContactFactory(DjangoModelFactory):

    contact = SubFactory(ContactFactory)
    email = Sequence(lambda n: "johndoe%d.example.com" % n)

    class Meta:
        model = Email
        django_get_or_create = ["email"]


class PhoneNumberContactFactory(DjangoModelFactory):

    contact = SubFactory(ContactFactory)
    phone_number = Sequence(lambda n: "+23320010569%d" % n)

    class Meta:
        model = PhoneNumber
        django_get_or_create = ["phone_number"]
