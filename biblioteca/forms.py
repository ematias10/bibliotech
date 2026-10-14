from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'autor',
            'isbn',
            'categoria',
            'precio_prestamo',
            'stock_copias',
            'fecha_publicacion',
            'disponible',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Don Quijote de la Mancha',
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Miguel de Cervantes',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 978-0142437230',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            'precio_prestamo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1500',
                'min': '0',
            }),
            'stock_copias': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 5',
                'min': '0',
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }