from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('admin/listado_autos', views.listado_autos, name='listado_autos'),
    path('admin/alta_autos', views.alta_autos, name='alta_autos'),
    path('editar_auto/<int:id>', views.editar_auto, name='editar_auto'),
    path('admin/eliminar_auto/<int:id>', views.eliminar_auto, name='eliminar_auto'),
    path('admin/crear_alquiler/<int:auto_id>', views.crear_alquiler, name='crear_alquiler'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('perdiste_Contraseña', views.perdiste_Contraseña, name='perdiste_Contraseña'),
    path('registrarse', views.registrarse, name='registrarse'), 
    
]