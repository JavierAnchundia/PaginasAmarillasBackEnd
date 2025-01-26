from django.db import models
from django.contrib.auth.models import AbstractUser


class Provincia(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    provincia = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return f"{self.provincia} -> {self.id}"

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
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField()
    state = models.CharField(choices=states, max_length=25, default=PENDIENTE, blank=True)
    
    def __str__(self) -> str:
        return f"{self.razon_social}"

class ProveedorProvincia(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, related_name="provincia_name", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.proveedor.razon_social} -> {self.provincia.provincia}"
class EnlaceProveedor(models.Model):

    FACEBOOK = "Facebook"
    INSTAGRAM = "Instagram"
    TIKTOK = "TikTok"
    X = "X"
    OTROS = "Otros"

    types = [
        (FACEBOOK, "Facebook"),
        (INSTAGRAM, "Instagram"),
        (TIKTOK, "TikTok"),
        (X, "X"),
        (OTROS, "Otros")

    ]

    id = models.AutoField(primary_key=True, unique=True)
    enlace = models.CharField(max_length=500)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    linkType = models.CharField(choices=types, max_length=500, default=OTROS, blank=True)

    def __str__(self) -> str:
        return f"{self.id} -> {self.proveedor.id_proveedor}] -> {self.proveedor.razon_social} -> {self.linkType}"

class ImagenProveedor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    image_path = models.ImageField(upload_to='proveedor/')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.proveedor.razon_social} -> {self.image_path}"

    def getprovincia(self):
        return self.provincia.all()


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
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        if self.subcategoria:
            return f"{self.categoria.nombre} -> {self.subcategoria.nombre}"
        else:
            return f"{self.categoria.nombre}"

class ProveedorCategoriaSubcategoria(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria_subcategoria = models.ForeignKey(CategoriaSubcategoria, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.proveedor.razon_social} -> {self.categoria_subcategoria.categoria.nombre}"




