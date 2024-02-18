from rest_framework import serializers
from .models import (
    Proveedor,
    ImagenProveedor,
    Categoria,
    Subcategoria,
    ProveedorCategoriaSubcategoria,
    CategoriaSubcategoria
)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = "__all__"

class CategoriaSubcategoriaSerializer(serializers.ModelSerializer):



    class Meta:
        model = CategoriaSubcategoria
        fields = ('categoria', 'subcategoria')

class ProveedorCategoriaSubcategoriaSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProveedorCategoriaSubcategoria
        fields =("proveedor", "categoria_subcategoria"    )

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ('id_proveedor' ,'ruc_cedula', 'razon_social', 'telefono', 'correo', 'provincia', 'ciudad',
                  'descripcion', 'state')


class ImageProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProveedor
        fields = "__all__"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
         # ...

        return token