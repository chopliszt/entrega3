from django import forms

from .models import Curso, Estudiante, Plan, Preferencia


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "email"]
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
            "preferencia_general",
        ]  # Excluyendo los otros campos por buena práctica
        widgets = {}


class CursoForm(forms.ModelForm):
    class Meta:
        model: Curso
        fields = ["nombre", "esta_activo"]
        widgets = {}


class PlanForm(forms.ModelForm):
    class Meta:
        model: Plan
        fields = ["nombre", "precio", "se_renueva"]
        widgets = {}
