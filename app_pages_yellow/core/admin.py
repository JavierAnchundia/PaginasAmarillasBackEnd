from django.contrib import admin
from .models import  Proveedor, ImagenProveedor, Categoria, CategoriaSubcategoria, Subcategoria, ProveedorCategoriaSubcategoria

admin.site.register([
     Proveedor, ImagenProveedor, Categoria, CategoriaSubcategoria, Subcategoria, ProveedorCategoriaSubcategoria
])
