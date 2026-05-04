from django.db import models
from locales.models import Local
 
 
class Evento(models.Model):
    nombre = models.CharField(max_length=250)
    fecha = models.DateField()
    hora = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=500, blank=True, null=True)
    estado = models.CharField(max_length=50)