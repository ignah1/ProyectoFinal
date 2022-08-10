from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CrearPost
def Inicio(request):
    return render(request, 'Blog/inicio.html')

def CrearP(request):
    if request.method == "POST":
        Formulario = CrearPost(request.POST)
        print(Formulario)
        if Formulario.is_valid:
            info = Formulario.cleaned_data
            info1 =info['Titulo']
            info2 =info['Subtitulo']
            info3 =info['Cuerpo']
            info4 =info['Autor']
            info5 =info['Fecha']
            POSTEAR = POSTEO(Titulo =info1 , Subtitulo =info2 , Cuerpo=info3, Autor=info4, Born=info5)
            POSTEAR.save()
            return render(request, 'Blog/inicio.html' , {"mensaje":f'Posteado Correctamente'})
    else:
        Formulario = CrearPost()

    return render(request, "Blog/CrearP.html", {"Crear":Formulario})

# Create your views here.
