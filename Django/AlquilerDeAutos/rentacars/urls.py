from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('listado_autos/', views.listado_autos, name='lista_autos'),
    path('alta_auto/', views.alta_auto, name='alta_auto'),
    # esta ruta es de prueba, contacto y alta_auto pueden heredar de este form
    path('formulario/', views.formulario, name='formulario'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('loguin/', views.loguin, name='loguin'),
    path('perdisteContraseña/', views.perdisteContraseña, name='perdisteContraseña'),
    path('registrarse/', views.registrarse, name='registrarse'),
    
]