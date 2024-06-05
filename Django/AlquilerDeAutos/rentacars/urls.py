from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listado_autos', views.listado_autos, name='listado_autos'),
    path('alta_autos', views.alta_autos, name='alta_autos'),
    path('editar_auto/<int:id>', views.editar_auto, name='editar_auto'),
    path('eliminar_auto/<int:id>', views.eliminar_auto, name='eliminar_auto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('perdiste_Contraseña', views.perdiste_Contraseña, name='perdiste_Contraseña'),
    path('registrarse', views.registrarse, name='registrarse'),
    
]