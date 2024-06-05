# Generated by Django 5.0.6 on 2024-06-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('patente', models.CharField(max_length=10, unique=True, verbose_name='Patente')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('imagen', models.CharField(verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('cuit', models.PositiveIntegerField(unique=True, verbose_name='CUIT')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
            ],
        ),
    ]
