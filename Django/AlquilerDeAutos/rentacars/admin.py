from django.contrib import admin
from .models import Alquiler, Usuario, Auto
# Register your models here.
admin.site.register(Alquiler)
admin.site.register(Usuario)
admin.site.register(Auto)