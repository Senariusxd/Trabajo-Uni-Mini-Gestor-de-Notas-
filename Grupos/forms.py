from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from .models import Estudiante
from .models import Asignatura

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'direccion', 'telefono']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AsignaturaForm(forms.ModelForm):
    semestre = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], error_messages={
            'invalid_choice': 'El semestre solo puede ser 1 o 2.',
            'max_value': 'El semestre debe ser 1 o 2.',
        })
    nombre = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Ingrese un nombre válido.')])

    class Meta:
        model = Asignatura
        fields = ['nombre', 'semestre', 'profesor_id_profesor']