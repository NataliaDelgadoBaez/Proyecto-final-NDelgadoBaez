from django.db import models
from django.contrib.auth.models import User


class Disco(models.Model):
    album = models.CharField(max_length=40)
    artista = models.CharField(max_length=40)
    año = models.IntegerField()
    precio = models.IntegerField()
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Producto(models.Model):
    album = models.CharField(max_length=40)
    artista = models.CharField(max_length=40)
    precio = models.IntegerField()
   
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)






