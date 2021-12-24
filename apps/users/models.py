from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validar_extension(valor):
    if not valor.name.enswith(settings.ALLOWED_IMG):
        raise ValidationError("Este formato de imagen no es valido")


class NewUser(AbstractUser):
    is_superuser = models.BooleanField(default= False)
    is_empleado = models.BooleanField(default= False)
