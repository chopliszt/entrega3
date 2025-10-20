from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=True)
    pass
