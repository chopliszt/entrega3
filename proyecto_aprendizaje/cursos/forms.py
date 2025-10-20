from django import forms

from .models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingresa tu nombre"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Ingresa tu correo"}
            ),
        }
