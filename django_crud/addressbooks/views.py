from rest_framework import filters, viewsets

from django_crud.addressbooks.models import Contact, Group

from .serializers import addressbook as ab


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ab.DetailContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(group__user=self.request.user)


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
