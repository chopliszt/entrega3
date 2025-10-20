from django.urls import path

from .views import crear_estudiante

urlpatterns = [
    path("crear-estudiante/", crear_estudiante, name="crear_estudiante"),
]
