from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_menu_manager = models.BooleanField(default=False)  # Grupo 1: Gerencia cardápios
    is_customer = models.BooleanField(default=True)       # Grupo 2: Faz reservas

    def __str__(self):
        return self.usernames