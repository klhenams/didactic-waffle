from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django_crud.addressbooks.models import Contact, Email, Group, PhoneNumber

from .serializers import addressbook as ab


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ab.ListContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(group__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = ab.CreateContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = ab.GroupSerializer
    queryset = Group.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmailContactViewSet(viewsets.ModelViewSet):
    serializer_class = ab.EmailSerializer
    queryset = Email.objects.all()

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(contact__group__user=self.request.user)

    @action(detail=True)
    def contact(self, request, pk=None):
        emails = self.queryset.filter(
            contact__group__user=self.request.user, contact=pk
        )
        return Response(self.serializer_class(emails, many=True).data)


class PhoneContactViewSet(EmailContactViewSet):
    serializer_class = ab.PhoneNumberSerializer
    queryset = PhoneNumber.objects.all()
