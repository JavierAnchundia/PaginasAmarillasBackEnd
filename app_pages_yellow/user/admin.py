from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdminConfig(UserAdmin):
    model = User

    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )
    fieldsets = (
        (
            "Información",
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password",
                )
            },
        ),
        ("Permisos", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)