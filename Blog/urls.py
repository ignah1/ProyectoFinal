from django.urls import path
from Blog import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('CrearP', views.CrearP, name="crearp"),
    path('VerPost/<TituloPost>', views.VerP, name='verp'),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request , name='logout'),
    path('editarperfil', views.editarperfil, name='editarperfil')
]