from django.shortcuts import render  # get_object_or_404

from .models import Estudiante

# Create your views here.


def index(request):
    return render(request, "cursos/index.html")
    pass


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "", {"estudiantes": estudiantes})
