from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    es_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions'
    )

# Modelo de Marca
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

# Modelo de Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

# Modelo de ModeloAuto
class ModeloAuto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} - {self.marca.nombre}"

# Modelo de Auto
class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo de FotoAuto
class FotoAuto(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='autos/')
    
    def __str__(self):
        return f"Foto de {self.auto.nombre}"

# Modelo de Cliente
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return self.usuario.username

# Modelo de Comentario
class Comentario(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.auto.nombre}"


