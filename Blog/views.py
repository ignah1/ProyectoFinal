from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CrearPost, UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required



def Inicio(request):
    POSTEOS = POSTEO.objects.all
   
    return render(request, 'Blog/inicio.html', {"POSTEOS":POSTEOS})


@login_required
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

def VerP(request, TituloPost):
    selec = POSTEO.objects.get(Titulo =TituloPost)   
    print(selec)
    contexto = {"jorge":selec}
    

    return(request, 'Blog/VerP.html', contexto)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            usuario = form.cleaned_data.get('username')

            contra = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contra)
            
            if user is not None:

                login(request, user)

                return render(request, "Blog/Inicio.html", {'form':form, "mensaje":f'Bienvenido {usuario}'})

            else:
                return render(request, "Blog/login.html", {'form':form, "mensaje":f'Error en loggeo'})

        else:
            return render(request, "Blog/login.html", {'form':form, "mensaje":f'Erorr en loggear'})

    form = AuthenticationForm()
    return render(request, "Blog/login.html", {'form':form}) 


def register(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Blog/Inicio.html" ,  {"mensaje":"Usuario Creado"})


      else:
            
            form = UserRegisterForm()     

      return render(request,"Blog/register.html" ,  {"form":form})


@login_required
def logout_request(request):
      logout(request)
      messages.info(request, "Saliste sin problemas")
      return redirect("inicio")


@login_required
def editarperfil(request):

      
      usuario = request.user
     
     
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "Blog/Inicio.html") 
     
      else: 
            
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      
      return render(request, "Blog/editarperfil.html", {"miFormulario":miFormulario, "usuario":usuario})


