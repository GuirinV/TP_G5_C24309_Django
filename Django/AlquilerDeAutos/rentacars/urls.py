from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registrarse/', views.registrarse, name='registrarse'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view, name='logout'),

    path('listado_autos/', views.listado_autos, name='listado_autos'),
    path('alta_autos/', views.alta_autos, name='alta_autos'),
    path('editar_auto/<int:id>/', views.editar_auto, name='editar_auto'),
    path('eliminar_auto/<int:id>/', views.eliminar_auto, name='eliminar_auto'),
    path('permission_denied/', views.permission_denied_view, name='permission_denied'),

    path('crear_alquiler/<int:auto_id>/', views.crear_alquiler, name='crear_alquiler'),
    path('listado_alquileres/', views.listado_alquileres, name='listado_alquileres'),
    path('editar_alquiler/<int:alquiler_id>/', views.editar_alquiler, name='editar_alquiler'),
    path('eliminar_alquiler/<int:alquiler_id>/', views.eliminar_alquiler, name='eliminar_alquiler'),
    path('get_precio_diario/<int:id>/', views.get_precio_diario, name='obtener_precio_alquiler'),
]