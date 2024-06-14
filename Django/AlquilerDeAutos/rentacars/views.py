from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .import forms 
from .forms import alta_autosForm
from  .models import Auto, Usuario, Alquiler
from .forms import AlquilerForm
from .forms import RegistrarseForm
from django.contrib.auth import login

# Otra opcion: from .forms import * (y se le quita forms abajo)

# Create your views here.

def obtener_autos():
    autos = Auto.objects.all()
    contexto = {'autos': autos}
    return contexto

def index(request):
    contexto = obtener_autos()
    # Accedo a la BBDD a traves de los modelos
    return render(request, 'rentacars/index.html', contexto)

def listado_autos(request):
    contexto = obtener_autos()
    return render(request, 'rentacars/listado_autos.html', contexto)

def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.marca = request.POST['marca']
        auto.modelo = request.POST['modelo']
        auto.color = request.POST['color']
        auto.precio = request.POST['precio']
        auto.imagen = request.POST['imagen']
        auto.save()
        return redirect('listado_autos')
    return render(request, 'rentacars/listado_autos.html')

def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('listado_autos')
    return render(request, 'rentacars/listado_autos.html')

def alta_autos(request):
    contexto = {}
    if request.method == "GET":
        contexto['alta_autos_form'] = alta_autosForm()
    else:
        form = alta_autosForm(request.POST)
        contexto['alta_autos_form'] = form  
        # Validar el formulario
        if form.is_valid():
            messages.success(request, 'El Auto fue dado de alta con éxito')
            nuevo_auto  = Auto(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                color=form.cleaned_data['color'],
                patente=form.cleaned_data['patente'],
                precio=form.cleaned_data['precio'],
                imagen = form.cleaned_data['imagen'] )
            nuevo_auto.save()

            return redirect('alta_autos')

    return render(request, 'rentacars/alta_autos.html', contexto)

def registrarse(request):
    contexto = {}
    if request.method == "GET":
        contexto['Registrarse_Form'] = RegistrarseForm()
    else:
        form = RegistrarseForm(request.POST)
        contexto['Registrarse_Form'] = form
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['nombre'],  
                last_name=form.cleaned_data['apellido'] 
            )
            nuevo_usuario = Usuario(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                cuit=form.cleaned_data['cuit'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono']
            )
            nuevo_usuario.save()
            login(request, user)  # Iniciar sesión automáticamente
            return redirect('index')
    return render(request, 'rentacars/registrarse.html', contexto)

@login_required
def crear_alquiler(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)

    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            alquiler = form.save(commit=False)
            usuario_auth = request.user
            try:
                usuario = Usuario.objects.get(user=usuario_auth)
                alquiler.usuario = usuario
                alquiler.auto = auto
                alquiler.save()
                messages.success(request, 'Alquiler creado con éxito.')
                return redirect('listado_alquileres')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuario no encontrado.')
        else:
            messages.error(request, 'Formulario no válido. Por favor, verifica los datos ingresados.')
    else:
        form = AlquilerForm()

    return render(request, 'rentacars/crear_alquiler.html', {'form': form, 'auto': auto})

def listado_alquileres(request):
    alquileres = Alquiler.objects.all()
    return render(request, 'rentacars/listado_alquileres.html', {'alquileres': alquileres})

def editar_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id)

    if request.method == 'POST':
        form = AlquilerForm(request.POST, instance=alquiler)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alquiler actualizado con éxito.')
            return redirect('listado_alquileres')
    else:
        form = AlquilerForm(instance=alquiler)

    return render(request, 'rentacars/editar_alquiler.html', {'form': form})

def eliminar_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id)

    if request.method == 'POST':
        alquiler.delete()
        messages.success(request, 'Alquiler eliminado con éxito.')
        return redirect('listado_alquileres')

    return render(request, 'rentacars/eliminar_alquiler.html', {'alquiler': alquiler})

def nosotros(request):
    contexto = {}
    return render(request, 'rentacars/nosotros.html', contexto)

def contacto(request):
    contexto = {}
    return render(request, 'rentacars/contacto.html', contexto)




def perdiste_Contraseña(request):
    contexto = {
        'perdiste_Contraseña_form' : forms.Perdiste_ContraseñaForm()
    }
    return render(request, 'rentacars/perdiste_Contraseña.html', contexto)
