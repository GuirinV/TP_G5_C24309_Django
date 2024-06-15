import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=100, verbose_name='Marca' )
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    color = models.CharField(max_length=50, verbose_name='Color')
    patente = models.CharField(max_length=10, verbose_name='Patente', unique=True)
    precio =  models.IntegerField(verbose_name='Precio')
    imagen = models.CharField(verbose_name='Imagen')

    def __str__(self):
        return f"Marca={self.marca}, modelo={self.modelo}"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    cuit = models.PositiveIntegerField(unique=True, verbose_name='CUIT')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')



# class Cliente(Usuario):
#     pass
# class Vendedor(Usuario):
#     pass


    def __str__(self):
        return f"Nombre={self.nombre}, apellido={self.apellido}"


class Alquiler(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name='Auto')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    fecha_inicio = models.DateField(default=timezone.now(), verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(default=timezone.now(), verbose_name='Fecha de fin')
    precio_total = models.FloatField(verbose_name='Precio total', blank=True)

    def __str__(self):
        return self.usuario + self.auto


