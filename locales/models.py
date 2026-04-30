from django.db import models


# Create your models here.
class Local(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    ubicacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    web = models.CharField(max_length=50)
    imagen = models.CharField(max_length=500, blank=True, null=True)
    estado = models.CharField(max_length=50)

   

