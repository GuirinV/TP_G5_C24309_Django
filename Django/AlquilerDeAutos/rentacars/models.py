from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=100, verbose_name='Marca' )
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    color = models.CharField(max_length=50, verbose_name='Color')
    patente = models.CharField(max_length=10, verbose_name='Patente', unique=True)
    precio =  models.IntegerField(verbose_name='Precio')
    imagen = models.CharField(verbose_name='Imagen')
    
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    cuit = models.PositiveIntegerField(unique=True, verbose_name='CUIT')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')

