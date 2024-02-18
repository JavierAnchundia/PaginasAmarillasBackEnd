from django.db import models
from django.contrib.auth.models import AbstractUser

class Proveedor(models.Model):
    INACTIVO = "Inactivo"
    PENDIENTE = "Pendiente"
    ACTIVO = "Activo"
    
    states = [
        (INACTIVO, "Inactivo"),
        (PENDIENTE, "Pendiente"),
        (ACTIVO, "Activo")
    ]

    id_proveedor = models.AutoField(primary_key=True)
    ruc_cedula = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    provincia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField()
    state = models.CharField(choices=states, max_length=25, default=PENDIENTE, blank=True)
    
    def __str__(self) -> str:
        return f"{self.razon_social}"

class ImagenProveedor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    image_path = models.ImageField(upload_to='proveedor/')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.proveedor.razon_social} -> {self.image_path}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    image_path = models.ImageField(upload_to='categoria/')
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class CategoriaSubcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.categoria.nombre} -> {self.subcategoria.nombre}"

class ProveedorCategoriaSubcategoria(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria_subcategoria = models.ForeignKey(CategoriaSubcategoria, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.proveedor.razon_social} -> {self.categoria_subcategoria.categoria.nombre}"


