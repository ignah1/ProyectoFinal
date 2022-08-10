from django.db import models
from ckeditor.fields import RichTextField


class POSTEO(models.Model):
    Titulo= models.CharField(max_length=30)
    Subtitulo= models.CharField(max_length=30)
    Cuerpo= RichTextField()
    Autor=models.CharField(max_length=30)
    Born=models.DateField() 

    def __str__(self):
        return f'{self.Titulo} por {self.Autor}' 
# Create your models here.
