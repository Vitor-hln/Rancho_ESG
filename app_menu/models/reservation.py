from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date
from .menu_models import Menu

class Reserva(models.Model):
     usuario = models.foreignkey(User, on_delete=models.CASCADE, verbose_name="Usuário")
     cardapio = models.foreingkey(Menu, on_delete=models.CASCADE, verbose_name="Cardápio")
     data_reserva = models.DateField(auto_now_add=True, verbose_name="Data da Reserva")


class Meta:
     verbose_name = "Reserva"
     verbose_name_plural = "Reservas"


def is_valid_reservation_date(self):
     """Verifica se a reserva é feita até 2 dias antes do cardápio"""
     return self.cardapio.data >= date.today() + timedelta(days=2)
