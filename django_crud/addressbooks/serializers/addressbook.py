from rest_framework import serializers

from django_crud.addressbooks.models import Contact, Email, Group, PhoneNumber


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ["email"]

    def to_representation(self, data):
        res = super().to_representation(data)
        return res["email"]


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ["phone_number"]

    def to_representation(self, data):
        res = super().to_representation(data)
        return res["phone_number"]


class DetailContactSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    email_set = EmailSerializer(read_only=True, many=True)
    phonenumber_set = PhoneNumberSerializer(read_only=True, many=True)

    class Meta:
        model = Contact
        fields = ["id", "group", "name", "email_set", "phonenumber_set"]
