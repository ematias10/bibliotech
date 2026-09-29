from .models import Libro
from django import forms

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder':'Escriba el titulo...'}),
        }