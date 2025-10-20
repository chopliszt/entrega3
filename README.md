# Proyecto de Aprendizaje con Django

Este proyecto es una aplicación web desarrollada con Django para gestionar cursos y estudiantes.

## Funcionalidades

- **Administración de Estudiantes**:
  - Crear, leer, actualizar y eliminar estudiantes.
  - Accesible en la interfaz de administración de Django y en la vista de la aplicación.

- **Administración de Cursos**:
  - Crear, leer, actualizar y eliminar cursos.
  - Accesible en la interfaz de administración de Django y en la vista de la aplicación.

- **Preferencias de Cursos**:
  - Asignar preferencias de cursos a los estudiantes.
  - Accesible en la vista de la aplicación.

## Orden para Probar las Funcionalidades

1. **Configuración Inicial**:
  - Asegúrate de tener todas las dependencias instaladas. Puedes instalar las dependencias con `pip install -r requirements.txt`.
  - Aplica las migraciones para configurar la base de datos: `python manage.py migrate`.

2. **Crear un Superusuario**:
  - Crea un superusuario para acceder a la interfaz de administración de Django: `python manage.py createsuperuser`.

3. **Acceder a la Interfaz de Administración**:
  - Inicia el servidor de desarrollo: `python manage.py runserver`.
  - Accede a la interfaz de administración en tu navegador: `http://127.0.0.1:8000/admin`.
  - Inicia sesión con las credenciales del superusuario que creaste.

4. **Probar las Funcionalidades en la Aplicación**:
  - Accede a la página principal de la aplicación.
  - Navega a las diferentes secciones para probar las funcionalidades de creación, lectura, actualización y eliminación de estudiantes y cursos.

5. **Probar las Funcionalidades de Preferencias**:
  - Accede a la sección de preferencias para asignar cursos a los estudiantes.

6. **Probar los Formularios**:
  - Accede a los formularios para crear estudiantes y cursos.
  - Envía los formularios para asegurarte de que los datos se guardan correctamente en la base de datos.

## Estructura del Proyecto

- `proyecto_aprendizaje/`: Directorio principal del proyecto Django.
- `cursos/`: Aplicación de cursos.
  - `models.py`: Define los modelos de la aplicación.
  - `views.py`: Define las vistas de la aplicación.
  - `forms.py`: Define los formularios de la aplicación.
  - `templates/`: Contiene las plantillas HTML de la aplicación.
  - `urls.py`: Define las rutas de la aplicación.
  - `admin.py`: Configura la interfaz de administración de Django para los modelos de la aplicación.

- `manage.py`: Script para gestionar el proyecto Django.

## Requisitos

- Python 3.x
- Django 5.x

## Instalación

1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Aplica las migraciones con `python manage.py migrate`.
4. Inicia el servidor de desarrollo con `python manage.py runserver`.

## Uso

1. Accede a la aplicación en tu navegador: `http://127.0.0.1:8000`.
2. Utiliza la interfaz de administración para gestionar los datos.
3. Utiliza los formularios en la vista de la aplicación para interactuar con los datos.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tus cambios: `git checkout -b mi-rama`.
3. Haz commit de tus cambios: `git commit -m "Descripción de los cambios"`.
4. Haz push a la rama: `git push origin mi-rama`.
5. Abre un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

