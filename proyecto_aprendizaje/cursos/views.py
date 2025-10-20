from django.shortcuts import redirect, render  # get_object_or_404

from .forms import EstudianteForm
from .models import Estudiante

# Create your views here.


def index(request):
    return render(request, "cursos/index.html")
    pass


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "", {"estudiantes": estudiantes})


def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # Mas adelante le agrego a donde deberian reenviarse
    else:
        form = EstudianteForm()

    return render(request, "cursos/crear_estudiante.html", {"form": form})
