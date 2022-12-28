from rest_framework import viewsets

from django_crud.addressbooks.models import Contact

from .serializers.addressbook import DetailContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = DetailContactSerializer
    queryset = Contact.objects.all()

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(group__user=self.request.user)
