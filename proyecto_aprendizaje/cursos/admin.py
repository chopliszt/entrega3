from django.contrib import admin

from .models import Curso, Estudiante, Plan

# Register your models here.
# Aqui por ejemplo uno pone los decoradores para que en el panel de admin uno pueda editar


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    pass


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass
