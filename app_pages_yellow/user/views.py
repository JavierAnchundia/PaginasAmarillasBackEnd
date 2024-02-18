from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .serializers import (
    ChangePasswordSerializer,
    Superadmin_Full_Serializer,
    User_Full_Serializer,
    CustomTokenSerializer,
)
from user import api

from django.utils import timezone


class LoginApiView(APIView):
    serializer_class = CustomTokenSerializer

    def post(self, request, format=None):
        user = api.validateAuth(request.data)

        serializer = self.serializer_class()
        tokens = serializer.get_token(user)
        user.last_login = timezone.now()
        user.save()

        return Response(tokens)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def information_user(request):

    if request.method == "GET":

        user = api.get_user_by_id(request.user.id)
        serializer = User_Full_Serializer(user)

        data = {"user": dict(serializer.data)}

        return Response(data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def user_api_view(request):

    if request.method == "GET":
        users = api.filter_user_by_key("is_staff", True)
        serializer = Superadmin_Full_Serializer(users, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        is_superuser = request.data.get("is_superuser")

        if is_superuser:
            user = api.enroll_superuser(request.data)
        else:
            user = api.enroll_admin(request.data)

        if user:
            return Response(
                {"msg": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED
            )

        return Response(
            {"msg": "Error al crear el usuario"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def user_detail_view(request, id):

    if request.method == "PUT":
        user = api.update_superuser(id, request.data)
        if user:
            return Response(
                {"msg": "Información actualizada correctamente"},
                status=status.HTTP_202_ACCEPTED,
            )

        return Response(
            {"msg": "Error al actualizar información el usuario"},
            status=status.HTTP_400_BAD_REQUEST,
        )
