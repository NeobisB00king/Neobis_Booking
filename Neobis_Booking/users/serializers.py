from rest_framework import serializers
from .models import User
# Roles
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login', 'name', 'email',)


# class RolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roles
#         fields = ('id', 'name',)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'login', 'email', 'name', 'surname', 'roles', 'phone', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        login = data.get()
        password = data.get()
        if login is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=login, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'login': user.login,
            'email': user.email,
            'token': user.token
        }


# class LoginSerializer(serializers.Serializer):
#     email    = serializers.CharField(max_length=128)
#     login = serializers.CharField(max_length=64, read_only=True)
#     password = serializers.CharField(max_length=64, write_only=True)
#     token    = serializers.CharField(max_length=256, read_only=True)
#
#     def validate(self, data):
#         email = data.get('email', None)
#         password = data.get('password', None)
#
#         if email is None:
#             raise serializers.ValidationError('An email address is required to log in.')
#
#         if password is None:
#             raise serializers.ValidationError('A password is required to log in.')
#
#         user = authenticate(username=email, password=password)
#
#         if user is None:
#             raise serializers.ValidationError('User not found.')
#
#         if not user.is_active:
#             raise serializers.ValidationError('This user has been deactivated.')
#
#         return {
#             'email':    user.email,
#             'username': user.login,
#             'token':    user.token
#         }