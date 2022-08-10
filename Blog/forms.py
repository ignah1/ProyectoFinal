from django import forms
from ckeditor.widgets import CKEditorWidget

class CrearPost(forms.Form):
    Titulo= forms.CharField()
    Subtitulo= forms.CharField()
    Cuerpo = forms.CharField(widget=CKEditorWidget())
    Autor=forms.CharField()
    Fecha=forms.DateField(widget=forms.SelectDateWidget())
