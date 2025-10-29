from django.contrib.auth.models import AbstractUser

# Create your models here.


class Perfil(AbstractUser):
    """
    Esta clase tendrá todo lo relacionado con los datos que  uno neesita del usuario. Por ejemplo:
    -usuario
    -Idiomas que quiere aprender
    -Idioma nativo
    nota: campos como el de apellido y nombre ya vienen directamente de la DB, entonces no es necesario repetirlos aquí
    """

    def __str__(self):
        return f"{self.first_name}"

    pass
