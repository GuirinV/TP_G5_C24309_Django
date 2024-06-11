from django import forms
from django.core.exceptions import ValidationError

class LoginForm (forms.Form):
    usuario = forms.CharField(label='Nombre de Usuario', required='True', widget=forms.TextInput(attrs={'class': 'input_clase2'}),label_suffix='')
    password= forms.CharField(label='Password', required='True',widget=forms.PasswordInput(attrs={'class': 'input_clase2'}),label_suffix='')

class Perdiste_ContraseñaForm (forms.Form):
    email = forms.EmailField(label='Email', required='True')

class RegistrarseForm (forms.Form):
    Nombre = forms.CharField(label='Nombre', required='True')
    Apellido = forms.CharField(label='Apellido', required='True')
    CUIT = forms.IntegerField(label='CUIT/CUIL', required='True')
    direccion = forms.CharField(label='Direccion', required='True')
    telefono = forms.IntegerField(label='Telefono', required='True')
    email = forms.EmailField(label='Email', required='True')
    usuario = forms.CharField(label='Nombre de Usuario', required='True')
    password= forms.CharField(widget=forms.PasswordInput)
    Confirmapassword= forms.CharField(widget=forms.PasswordInput)


class alta_autosForm(forms.Form):
    marca = forms.CharField(label='Marca', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    modelo = forms.CharField(label='Modelo', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    color = forms.CharField(label='Color', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    patente = forms.CharField(label='Patente', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='')
    precio = forms.CharField(label='Precio', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='') 
    imagen = forms.CharField(label='Imagen', required=True, widget=forms.TextInput(attrs={'class': 'input_clase'}),label_suffix='' )
    def clean_Marca(self):
        marca = self.cleaned_data['marca']
        if not marca.isalpha():
            raise ValidationError("La Marca solo puede estar compuesta por letras")
        return self.cleaned_data['Marca']

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
