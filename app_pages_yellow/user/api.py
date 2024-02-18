from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


def get_users():
    users = User.objects.all().order_by("username")
    return users


def exists_user_by_id(id):
    user = User.objects.filter(id=id)
    return user.exists()


def get_user_by_id(id):
    try:
        user = User.objects.get(id=id)
        return user
    except Exception:
        return None


def filter_user_by_key(key, value):
    if key == "id":
        return User.objects.filter(id=value)
    elif key == "is_staff":
        return User.objects.filter(is_staff=value).order_by("first_name")
    elif key == "email":
        return User.objects.filter(email=value)


def enroll_superuser(data):
    user = User.objects.create_superuser(
        data.get("email"),
        data.get("first_name"),
        data.get("last_name"),
        data.get("password"),
    )
    user.full_clean()
    user.save()
    return user


def enroll_admin(data):
    user = User.objects.create_superuser(
        data.get("email"),
        data.get("first_name"),
        data.get("last_name"),
        data.get("password"),
    )
    user.is_superuser = False
    user.full_clean()
    user.save()
    return user


def is_email_available(email):
    user = User.objects.filter(email=email)
    return user.exists()


def update_user(user, data):
    user.first_name = data.get("first_name")
    user.last_name = data.get("last_name")

    if "password" in data:
        user.set_password(data.get("password"))

    user.save()
    return user


def update_superuser(id, data):
    user = get_user_by_id(id)
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user.is_active = data.get("is_active", user.is_active)
    user.is_superuser = data.get("is_superuser", user.is_superuser)
    user.email = data.get("email", user.email)

    if "password" in data:
        if data["password"] != "" and data["password"] != None:
            user.set_password(data.get("password"))

    user.save()
    return user


def validateAuth(data):
    email = data.get("email")
    password = data.get("password")

    if password is None:
        raise AuthenticationFailed("Contraseña inválida")

    validateActiveUser = User.objects.filter(email=email)

    if not validateActiveUser.exists():
        raise AuthenticationFailed("Error de cuenta")

    user = validateActiveUser.first()

    if not user.is_active:
        raise AuthenticationFailed("Cuenta inactiva")

   
    user_auth = auth.authenticate(email=email, password=password)

    if not user_auth:
        raise AuthenticationFailed("Credenciales Inválidas")

    return user

