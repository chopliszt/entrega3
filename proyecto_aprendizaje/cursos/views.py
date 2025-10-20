from django.shortcuts import redirect, render  # get_object_or_404

from .forms import CursoForm, EstudianteForm, PlanForm, PreferenciaForm
from .models import Estudiante

# Create your views here.


def index(request):
    """ """
    return render(request, "cursos/index.html")


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


def crear_plan(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # Mas adelante le agrego a donde deberian reenviarse
    else:
        form = PlanForm()

    return render(request, "cursos/crear_plan.html", {"form": form})


def crear_preferencia(request):
    if request.method == "POST":
        form = PreferenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # Mas adelante le agrego a donde deberian reenviarse
    else:
        form = PreferenciaForm()

    return render(request, "cursos/crear_preferencia.html", {"form": form})


def crear_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # Mas adelante le agrego a donde deberian reenviarse
    else:
        form = CursoForm()

    return render(request, "cursos/crear_curso.html", {"form": form})
