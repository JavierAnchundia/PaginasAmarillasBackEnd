from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import User


class User_Full_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "is_staff",
            "is_superuser",
            "last_login",
        ]


class Superadmin_Full_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
        ]


class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        refresh = token
        access = token.access_token
        access["name"] = "{} {}".format(user.first_name, user.last_name)
        access["is_staff"] = user.is_staff
        
        return {
            "refresh": str(refresh),
            "access": str(access),
            "is_staff": user.is_staff,
        }


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)