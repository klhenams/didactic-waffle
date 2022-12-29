from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory

from django_crud.addressbooks.models import Group
from django_crud.users.tests.factories import UserFactory


class GroupFactory(DjangoModelFactory):

    user = SubFactory(UserFactory)
    name = Sequence(lambda n: "Group %d" % n)

    class Meta:
        model = Group
        django_get_or_create = ["name"]
