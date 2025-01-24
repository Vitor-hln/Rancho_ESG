from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    obsercacoes = models.TextField(null= True, blank=True)
    # (null= True, blank=True) - não obrigatório

    class Meta: # define o nome no plural da classe
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.descricao
