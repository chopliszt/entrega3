from django import forms

from .models import Estudiante, Preferencia


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


class PreferenciaForm(forms.ModelForm):
    class Meta:
        model = Preferencia
        fields = [
            "curso",
            "preferences_field1",
            "preferences_field2",
        ]  # Excluyendo el campo de estudiante
