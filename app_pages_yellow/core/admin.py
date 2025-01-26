from django.contrib import admin
from .models import  (Proveedor, ImagenProveedor, Categoria, CategoriaSubcategoria, Subcategoria,
                      ProveedorCategoriaSubcategoria, Provincia, ProveedorProvincia, EnlaceProveedor)

admin.site.register([
     Proveedor, ImagenProveedor, Categoria, CategoriaSubcategoria, Subcategoria, ProveedorCategoriaSubcategoria, Provincia,
    ProveedorProvincia, EnlaceProveedor
])
