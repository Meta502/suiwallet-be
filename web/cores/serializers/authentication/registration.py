from rest_framework import serializers

class RegistrationRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)
    email = serializers.CharField(max_length=128)
    nik = serializers.CharField(max_length=16)
    birth_date = serializers.DateTimeField()
    phone_number = serializers.CharField(max_length=64)
    address = serializers.CharField(max_length=1024)
    postal_code = serializers.CharField(max_length=16)


class RegistrationResponseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    email = serializers.CharField(max_length=256)

