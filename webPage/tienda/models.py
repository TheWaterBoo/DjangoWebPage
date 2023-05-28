from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcin = models.TextField()
    precio = models.DecimalField(max_digits=8)