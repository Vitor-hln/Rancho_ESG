from contextlib import nullcontext
from django.db import models
from django.core.validators import validate_email
# Utilizar após saber o dominio do email utilizado na ESG
"""from django.core.exceptions import ValidationError    
from django.utils.translation import gettext_lazy as _

def validar_email_personalizado(value):
    if not value.endswith('@exemplo.com'):
        raise ValidationError(
            _('Somente e-mails do domínio @exemplo.com são permitidos.'),
            params={'value': value},
        )"""

class Usuario(models.Model):
    nome = models.CharField(max_length=100,
                            null= False,
                            blank = False,
                            verbose_name = "Nome")
    matricula = models.CharField(max_length= 30, verbose_name = "Matricula")
    data_criacao = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length = 254,
                             unique=True,
                             null=False,
                             blank=False,
                             verbose_name= "E-mail Institucional",
                             validators = [validate_email],
                             error_messages={'invalid': "Por favor, insira um e-mail válido."}
                             )

    def __str__(self):
        return self.nome
