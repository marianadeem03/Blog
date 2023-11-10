from rest_framework import serializers
from users.models import User
from django.contrib.auth import password_validation


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)

        user.set_password(password)
        user.is_active = False
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password", "role_types"]
