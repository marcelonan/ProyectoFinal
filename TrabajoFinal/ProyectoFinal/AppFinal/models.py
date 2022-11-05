from django.db import models

# Create your models here.
class productos(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class reseñas(models.Model):

    nombre = models.CharField(max_length=50)
    reseña = models.CharField(max_length=50)

class tienda(models.Model):
    dias = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)