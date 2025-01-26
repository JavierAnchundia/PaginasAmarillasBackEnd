from rest_framework import serializers
from .models import (
    Proveedor,
    ImagenProveedor,
    Categoria,
    Subcategoria,
    ProveedorCategoriaSubcategoria,
    CategoriaSubcategoria,
    Provincia,
    EnlaceProveedor,
    ProveedorProvincia
)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = "__all__"

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

class ProveedorProvinciaSerializer(serializers.ModelSerializer):
    provincia_name = serializers.CharField(source='provincia.provincia', allow_blank=True)

    class Meta:
        model = ProveedorProvincia
        fields =("proveedor", "provincia", "provincia_name")

class ProveedorProvinciaSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = ProveedorProvincia
        fields =("proveedor", "provincia")

class ProveedorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Proveedor
        fields = ('id_proveedor' ,'ruc_cedula', 'razon_social', 'telefono', 'correo', 'ciudad',
                  'descripcion', 'state')


class ImageProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProveedor
        fields = "__all__"

class EnlaceProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnlaceProveedor
        fields = "__all__"
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
         # ...

        return token



