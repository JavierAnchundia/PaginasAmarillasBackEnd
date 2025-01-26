from rest_framework.decorators import api_view, permission_classes

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

from core import api 


@api_view(["GET", "POST"])
# @permission_classes([IsAutphenticated])
def proveedorActivoAll_api_view(request):

    if request.method == "GET":
        resp = api.list_Activeproveedor()
        return Response(resp)

    if request.method == "POST":
        resp = api.create_proveedor(request.data)
        
        if resp:
            return Response(
                {"msg": "Se ha registrado correctamente el proveedor"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"msg": "No se ha podido registrar el proveedor"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET", "POST"])
def proveedorActivoFilter_api_view(request):


    if request.method == "POST":

        resp = api.list_filterproveedor(request.data)
        return Response(resp)

@api_view(["GET", "POST"])
def proveedorPostulante_api_view(request):
    if request.method == "GET":
        resp = api.list_Postulanteproveedor()
        return Response(resp)

    if request.method == "POST":
        resp = api.create_proveedor(request.data)

        if resp:
            return Response(
                {"msg": "Se ha registrado correctamente el proveedor",
                 "data": resp
                 },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"msg": "No se ha podido registrar el proveedor"},
            status=status.HTTP_400_BAD_REQUEST,
        )



@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
def categoria_by_proveedor_api_view(request, proveedor_id):

    if request.method == "GET":
        resp = api.list_categoria_subcategoria(proveedor_id)
        return Response(resp)
      
@api_view(["GET", "PUT"])
def proveedorActivoSet_api_view(request, pk):

    if request.method == "GET":
        resp = api.getProveedorById(request, pk)
        return Response(resp)

    if request.method == "PUT":
        resp = api.editProveedor(request.data, pk)

        if resp:
            print("Hola")
            return Response(
                {"msg": "Se ha modificado correctamente el proveedor"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"msg": "No se ha podido modificar el proveedor"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET", "POST"])
def imagenProveedor_api_view(request):


    if request.method == "POST":
        print("Mi request")
        print(request)
        resp = api.create_image_proveedor(request.data)

        if resp:
            return Response(
                {"msg": "Se ha registrado correctamente el proveedor"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"msg": "No se ha podido registrar el proveedor"},
            status=status.HTTP_400_BAD_REQUEST,
        )



@api_view(["GET"])
def categorias_api_view(request):

    if request.method == "GET":
        resp = api.getCategorias()
        return Response(resp)


@api_view([ "POST"])
# @permission_classes([IsAuthenticated])
def subcategoriaByCategoria_api_view(request):

    if request.method == "POST":
        resp = api.list_subcategoriasByCategoria(request.data)
        return Response(resp)


@api_view([ "POST"])
# @permission_classes([IsAuthenticated])
def crearProveedorCategoriaSubcategoria_api_view(request):

    if request.method == "POST":
        resp = api.create_proveedorCategoriaSubcategoria(request.data)
        return Response(resp)

@api_view([ "POST"])
# @permission_classes([IsAuthenticated])
def crearProveedorProvinciasa_api_view(request):

    if request.method == "POST":
        resp = api.create_proveedorProvincia(request.data)
        return Response(resp)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def provincias_api_view(request):

    if request.method == "GET":
        resp = api.getProvincias()
        return Response(resp)

@api_view(["PUT"])
def proveedorProvincia_api_view(request, pk ):
    print("Hola  dentro del Delete 2")

    #This method will delete the registers of ProveedorProvincia that coincides with the list of provinces and the provider id
    if request.method == "PUT":
        resp = api.deleteProveedorProvincia(request.data, pk)

        if resp:
            print("Hola  dentro del Delete")
            return Response(
                {"msg": "Se ha eliminado las provincias del Proveedor"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"msg": "No se ha podido eliminar las provincias del proveedor"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PUT"])
def proveedorEnlacesDelete_api_view(request, pk ):
    print("Hola  dentro del Delete Enlaces")

    #This method will delete the registers of ProveedorProvincia that coincides with the list of provinces and the provider id
    if request.method == "PUT":
        resp = api.deleteProveedorEnlaces(request.data, pk)

        if resp:
            print("Hola  dentro del Delete")
            return Response(
                {"msg": "Se han eliminado los enlaces seleccionados del Proveedor"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"msg": "No se ha podido eliminar los enlaces del proveedor"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def enlaces_api_view(request):

    if request.method == "GET":
        resp = api.getAllEnlaces()
        return Response(resp)


@api_view([ "PUT"])
# @permission_classes([IsAuthenticated])
def crearProveedorEnlaces_api_view(request, pk):

    if request.method == "PUT":
        resp = api.create_proveedorEnlaces(request.data, pk)
        return Response(resp)