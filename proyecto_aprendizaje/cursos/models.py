import uuid

from django.db import models
from django.utils import timezone

# Create your models here.


# Necesito saber si está activo, porque el plan sería general
class Curso(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=True, unique=True)
    fecha_creado = models.DateTimeField(default=timezone.now)
    esta_activo = models.BooleanField(default=False)
    # Tags, agregar en el futuro


class Plan(models.Model):
    """
    Esta clase modela el plan de pagos. Se pueden tener diferentes tipos de pagos como una recarga prepago, una membresía mensual, etc
    """

    nombre = models.CharField(max_length=150, null=False, blank=True, unique=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    se_renueva = models.BooleanField(default=False)


class Estudiante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_actualizado = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=150, null=False, blank=True)
    email = models.EmailField(
        max_length=254, unique=True, null=False, blank=False
    )  # unique sirve para que en la DB el registro se unico

    def __str__(self):
        return f"{self.nombre}, creado el {self.fecha_creado}"


class Preferencia(models.Model):
    """
    Esta clase modela que un estudiante, a un curso especifico tenga ciertas preferencias. Por ejemplo, la estudiante Ana quiere aprender Japonés, porque le gusta el anime y prefiere aprender con humor. También sabe que tiene ciertos temas que quiere mejorar.
    """

    preferencia_general = models.TextField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Preferencias de {self.estudiante.nombre} para curso: son preferencias: {self.preferencia_general}"
