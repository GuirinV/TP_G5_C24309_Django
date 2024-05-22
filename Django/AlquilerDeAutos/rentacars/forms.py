from django import forms

class LoginForm (forms.Form):
    usuario = forms.CharField(label='Nombre de Usuario', required='True')
    password= forms.CharField(widget=forms.PasswordInput)

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