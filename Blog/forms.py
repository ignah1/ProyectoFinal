from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

class CrearPost(forms.Form):
    Titulo= forms.CharField()
    Subtitulo= forms.CharField()
    Cuerpo = forms.CharField(widget=CKEditorWidget())
    Autor=forms.CharField()
    Fecha=forms.DateField(widget=forms.SelectDateWidget())


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):


    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}
