from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=100, verbose_name='Marca' )
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    color = models.CharField(max_length=50, verbose_name='Color')
    patente = models.CharField(max_length=10, verbose_name='Patente', unique=True)
    precio =  models.IntegerField(verbose_name='Precio')
    imagen = models.CharField(verbose_name='Imagen')
    
    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.patente})'
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    cuit = models.PositiveIntegerField(unique=True, verbose_name='CUIT')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    usuario = models.CharField(max_length=100, verbose_name='Nombre de Usuario')
    password = models.CharField(max_length=100, verbose_name='Contraseña')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alquiler(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name='Auto')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(verbose_name='Fecha de fin')
    precio_total = models.IntegerField(verbose_name='Precio total')

    def __str__(self):
        return f"Auto: {self.auto} ,Cliente: {self.usuario} , Fecha inicio: {self.fecha_inicio} ,fecha Entrega: {self.fecha_fin}"
