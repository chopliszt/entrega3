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
            "curso",
        ]  # Excluyendo los otros campos por buena práctica
        widgets = {
            "preferencia_general": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingresa tus preferencias",
                }
            ),
            "curso": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre", "esta_activo"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del curso. Ej: Alemán",
                }
            ),
            "esta_activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ["nombre", "precio", "se_renueva"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del plan. Ej: Plan Premium",
                }
            ),
            "precio": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Precio del plan"}
            ),
            "se_renueva": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
