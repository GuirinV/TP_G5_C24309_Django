from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listado_autos', views.listado_autos, name='lista_autos'),
     path('alta_autos', views.alta_autos, name='alta_autos'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('perdiste_Contraseña', views.perdiste_Contraseña, name='perdiste_Contraseña'),
    path('registrarse', views.registrarse, name='registrarse'),
    
]