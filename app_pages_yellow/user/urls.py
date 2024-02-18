from django.urls import path
from .views import (
    LoginApiView,
    information_user,
    user_api_view,
    user_detail_view,
)

urlpatterns = [
    path("login/", LoginApiView.as_view()),
    path("information/", information_user),
    path("superadmin/", user_api_view),
    path("superadmin/<str:id>/", user_detail_view),
]