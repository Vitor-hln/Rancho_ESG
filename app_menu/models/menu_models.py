from datetime import date

from django.db import models

class Menu(models.Model):
    data = models.DateField(unique=True, verbose_name="Data")
    carbs = models.TextField(Verbose_name="Carboidrato")
    protein = models.TextField(verbose_name="Proteína")
    vegetables = models.TextField(verbose_name="Legumes")
    beverages = models.TextField(verbose_name="Bebidas")
    dessert = models.TextField(Verbose_name="Sobremesa")

    class Meta:
        verbose_name = "Cardápio"
        verbose_name_plural = "Cardápios"
        ordering = ["-data"]

    def __str__(self):
        return f"Cardápio de {self.data.strft3ime('%d/%m/%Y')}"

    def is_updatable(self):
        """Verifica se o cardápio pode ser atualizado no dia da exibição"""
        return self.data == date.today()


