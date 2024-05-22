from django import forms

class LoginForm (forms.Form):
    usuario = forms.CharField(label='Nombre de Usuario', required='True')
    password= forms.CharField(widget=forms.PasswordInput)

class ContraseñaForm (forms.Form):
    email = forms.EmailField(label='Email', required='True')


class RegistrarseForm (forms.Form):
    usuario = forms.CharField(label='Nombre de Usuario', required='True')
    email = forms.EmailField(label='Email', required='True')