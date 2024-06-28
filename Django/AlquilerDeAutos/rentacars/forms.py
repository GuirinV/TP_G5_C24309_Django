
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils import timezone

from .models import Alquiler, Auto
from django.contrib.auth.models import User


class LoginForm (forms.Form):
    username = forms.CharField(label='Nombre de Usuario', required=True, widget=forms.TextInput(attrs={'class': 'input_clase2'}),label_suffix='')
    password= forms.CharField(label='Password', required=True,widget=forms.PasswordInput(attrs={'class': 'input_clase2'}),label_suffix='')

class Perdiste_ContraseñaForm (forms.Form):
    email = forms.EmailField(label='Email', required=True)

class RegistrarseForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=100)
    cuit = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'nombre', 'apellido', 'cuit', 'direccion', 'telefono']

class alta_autosForm(forms.Form):
    marca = forms.CharField(label='Marca', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    modelo = forms.CharField(label='Modelo', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    color = forms.CharField(label='Color', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    patente = forms.CharField(label='Patente', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    precio = forms.CharField(label='Precio', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='') 
    imagen = forms.CharField(label='Imagen', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    def clean_Marca(self):
        marca = self.cleaned_data['marca']
        if not marca.isalpha():
            raise ValidationError("La Marca solo puede estar compuesta por letras")
        return self.cleaned_data['Marca']
    
    def clean_patente(self):
        patente = self.cleaned_data['patente']
        if Auto.objects.filter(patente=patente).exists():
            raise ValidationError("Ya existe un auto con esta patente")
        return patente
    
    def clean_Precio(self):
        precio = self.cleaned_data['precio']
        # Intenta convertir el precio a un entero
        try:
            precio_entero = int(precio)
        except ValueError:
            raise ValidationError("El Precio solo puede estar compuesto por números")
        return precio_entero
    
    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data

class AlquilerForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'value': timezone.now().strftime('%d/%m/%Y')}),
        initial=timezone.now().strftime('%Y-%m-%d'),  # Usar timezone.now().date para obtener la fecha actual
        label="Inicio de alquiler: "
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'value': timezone.now().strftime('%d/%m/%Y')}),
        initial=timezone.now().strftime('%Y-%m-%d'),  # Usar timezone.now().date para obtener la fecha actual
        label="Fin de Alquiler: "
    )

    class Meta:
        model = Alquiler
        fields = ['fecha_inicio', 'fecha_fin', 'precio_total']
        # widgets = {
        #     'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        #     'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['precio_total'].disabled = True

