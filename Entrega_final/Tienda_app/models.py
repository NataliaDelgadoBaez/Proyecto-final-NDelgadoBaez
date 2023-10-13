from django.db import models

class Disco(models.Model):
    album = models.CharField(max_length=40)
    artista = models.CharField(max_length=40)
    año = models.IntegerField()
    precio = models.IntegerField()
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Usuario_vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
   






