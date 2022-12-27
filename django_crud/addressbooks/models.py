from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Group(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Email(models.Model):
    """Add extra fields like slug or type to describe or tag email eg. official or personal etc"""

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        unique_together = ["contact", "email"]

    def __str__(self):
        return self.email


class PhoneNumber(models.Model):
    """Add extra fields like slug or type to describe or tag phone number eg. office or home etc"""

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()

    class Meta:
        unique_together = ["contact", "phone_number"]

    def __str__(self):
        return self.phone_number
