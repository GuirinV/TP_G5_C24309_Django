import datetime

from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class Auto(models.Model):
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    color = models.CharField(max_length=50, verbose_name='Color')
    patente = models.CharField(max_length=10, verbose_name='Patente', unique=True)
    precio = models.IntegerField(verbose_name='Precio')
    imagen = models.CharField(verbose_name='Imagen')

    def __str__(self):

        return f"Marca={self.marca}, modelo={self.modelo}"


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    cuit = models.PositiveIntegerField(unique=True, verbose_name='CUIT')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    # email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    # username = models.CharField(max_length=100, verbose_name='Nombre de Usuario')
    # password = models.CharField(max_length=100, verbose_name='Contraseña')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # No es necesario porque no editamos el usuario!
    # def save(self, *args, **kwargs):
    #     # Actualiza los campos first_name y last_name del usuario
    #     # self.user.first_name = self.nombre
    #     # self.user.last_name = self.apellido
    #     # Si la contraseña ha cambiado, asegúrate de encriptarla
    #     # if not self.user.check_password(self.password):
    #     #     self.user.set_password(self.password)
    #     # self.user.save()
    #     super().save(*args, **kwargs)

class Alquiler(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name='Auto')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')

    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(verbose_name='Fecha de fin')
    precio_total = models.FloatField(verbose_name='Precio total', blank=True)

    def __str__(self):
        return f"Auto: {self.auto} ,Cliente: {self.usuario} , Fecha inicio: {self.fecha_inicio} ,fecha Entrega: {self.fecha_fin}, total: {self.precio_total}"


Auto.usuarios = models.ManyToManyField(Usuario, through=Alquiler, related_name='autos')
Usuario.autos = models.ManyToManyField(Auto, through=Alquiler, related_name='usuarios')

