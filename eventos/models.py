from django.db import models
from locales.models import Local


# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=250)
    fecha = models.DateField()
    hora = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='images/eventos/')
    estado = models.CharField(max_length=50)



