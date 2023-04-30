from rest_framework import serializers

class RegistrationRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)
    email = serializers.CharField(max_length=128)


class RegistrationResponseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    email = serializers.CharField(max_length=256)

