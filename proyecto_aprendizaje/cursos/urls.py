from django.urls import path

from .views import crear_curso, crear_estudiante, crear_plan, crear_preferencia

urlpatterns = [
    path("crear-estudiante/", crear_estudiante, name="crear_estudiante"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("crear-plan/", crear_plan, name="crear_plan"),
    path("crear-preferencia/", crear_preferencia, name="crear_preferencia"),
]
