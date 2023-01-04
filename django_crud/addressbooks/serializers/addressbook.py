from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from django_crud.addressbooks.models import Contact, Email, Group, PhoneNumber


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ["id", "contact", "email"]


class BaseContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "group", "name"]


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ["id", "contact", "phone_number"]


class ListEmailSerializer(EmailSerializer):
    def to_representation(self, data):
        res = super().to_representation(data)
        return res["email"]


class ListPhoneNumberSerializer(PhoneNumberSerializer):
    def to_representation(self, data):
        res = super().to_representation(data)
        return res["phone_number"]


class ContactSerializer(serializers.ModelSerializer):
    email_set = None
    phonenumber_set = None

    class Meta:
        model = Contact
        fields = ["id", "group", "name", "email_set", "phonenumber_set"]


class ListContactSerializer(ContactSerializer):
    group = GroupSerializer()
    email_set = ListEmailSerializer(read_only=True, many=True)
    phonenumber_set = ListPhoneNumberSerializer(read_only=True, many=True)


class CreateContactSerializer(ContactSerializer):
    email_set = serializers.ListField(
        child=serializers.EmailField(), required=False, write_only=True
    )
    phonenumber_set = serializers.ListField(
        child=PhoneNumberField(), required=False, write_only=True
    )

    def create(self, validated_data):
        email_set = validated_data.pop("email_set", None)
        phonenumber_set = validated_data.pop("phonenumber_set", None)
        self.contact = super().create(validated_data)
        assert isinstance(self.contact, Contact)
        if email_set is not None:
            self._create_email(email_set)
        if phonenumber_set is not None:
            self._create_phonenumber(phonenumber_set)
        return self.contact

    def _create_email(self, email_set: list):
        try:
            Email.objects.bulk_create(
                [Email(contact=self.contact, email=email) for email in email_set]
            )
        except Exception as err:  # noqa: F841
            # TODO: handle exceptions here
            pass

    def _create_phonenumber(self, phonenumber_set: list):
        try:
            PhoneNumber.objects.bulk_create(
                [
                    Email(ccontact=self.contact, phone_number=phonenumber)
                    for phonenumber in phonenumber_set
                ]
            )
        except Exception as err:  # noqa: F841
            # TODO: handle exceptions here
            pass
