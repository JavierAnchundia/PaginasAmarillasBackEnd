from django.urls import path
from .views import (categoria_by_proveedor_api_view, proveedorActivoAll_api_view,
                    proveedorPostulante_api_view, proveedorActivoFilter_api_view,
                    proveedorActivoSet_api_view,imagenProveedor_api_view, categorias_api_view, subcategoriaByCategoria_api_view,
                    crearProveedorCategoriaSubcategoria_api_view,MyTokenObtainPairView, provincias_api_view, crearProveedorProvinciasa_api_view,proveedorProvincia_api_view,
                    enlaces_api_view, crearProveedorEnlaces_api_view, proveedorEnlacesDelete_api_view)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('proveedores_activosAll', proveedorActivoAll_api_view),
    path('proveedores_postulantes', proveedorPostulante_api_view),
    path('proveedoresFilter_activos', proveedorActivoFilter_api_view),
    path('proveedorSetRegistro/<str:pk>/', proveedorActivoSet_api_view),
    path('imagen_proveedor', imagenProveedor_api_view),
    path('categorias', categorias_api_view),
    path('subcategorias', subcategoriaByCategoria_api_view),
    path('proveedorCategoriasSubcategorias', crearProveedorCategoriaSubcategoria_api_view),
    path('proveedorProvincias', crearProveedorProvinciasa_api_view),
    path('proveedorProvinciasViewSet/<str:pk>/', proveedorProvincia_api_view),
    path('provincias', provincias_api_view),
    path('enlaces', enlaces_api_view),
    path('proveedorEnlaces/<str:pk>/', crearProveedorEnlaces_api_view),
    path('proveedorEnlacesDelete/<str:pk>/', proveedorEnlacesDelete_api_view),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('category_by_proveedor/<str:proveedor_id>/', categoria_by_proveedor_api_view)
]