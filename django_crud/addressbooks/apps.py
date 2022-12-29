from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddressbooksConfig(AppConfig):
    name = "django_crud.addressbooks"
    verbose_name = _("Address Books")
