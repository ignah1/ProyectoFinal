from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('CrearP', views.CrearP, name="crearp"),

]