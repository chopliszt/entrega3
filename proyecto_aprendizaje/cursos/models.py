from django.db import models

# Create your models here.


class Curso(models.Model):
    pass


class Plan(models.Model):
    pass


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=True)
    email = models.EmailField(
        max_length=254, unique=True, null=False, blank=False
    )  # unique sirve para que en la DB el registro se unico

    def __str__(self):
        return f"{self.nombre}"
