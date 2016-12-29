from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=20,
                               error_messages = {'required': 'El username es obligatorio.', 'unique': 'El correo electronico ya esta registrado.' , 'invalid': 'El username no es valido.'})
    password = forms.CharField(max_length=20, widget=forms.PasswordInput,
                               error_messages={'required': 'El password es obligatorio.'})
    email = forms.CharField(error_messages = {'required': 'El correo electronico es obligatorio.', 'unique': 'El correo electronico ya esta registrado.', 'invalid': 'El correo electronico no es valido.'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
