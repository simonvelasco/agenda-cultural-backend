from django.db import models


# Create your models here.
class Local(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    ubicacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    web = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='images/locals/')
    estado = models.CharField(max_length=50)

   

