from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager para usuarios"""

    def create_user(self, email, first_name, last_name, username, password ):
        """Crear nuevo usuario"""

        if not email:
            raise ValueError("Email es Requerido")

        email = self.normalize_email(email)
        # username = self.get_username(email)

        user = self.model(
            email=email, first_name=first_name, last_name=last_name, username=username
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name,  last_name, username, password):
        user = self.create_user(email, first_name, last_name, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    # def get_username(self, email):
    #     return email.split("@")[0]


class User(AbstractBaseUser, PermissionsMixin):
    """Modelo Base de datos para Usuarios del sistema"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "password"]

    def get_full_name(self):
        """Obtener nombre completo del Usuario"""
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        """Retornar nombre de usuario"""
        return self.username