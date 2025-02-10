from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  AbstractUser
#from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


# Utilizar após saber o dominio do e-mail utilizado na ESG
"""from django.core.exceptions import ValidationError    
from django.utils.translation import gettext_lazy as _

def validar_email_personalizado(value):
    if not value.endswith('@exemplo.com'):
        raise ValidationError(
            _('Somente e-mails do domínio @exemplo.com são permitidos.'),
            params={'value': value},
        )"""

class CustomUser(AbstractUser):
    is_menu_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class RegistrationForm(UserCreationForm):
    is_menu_manager = forms.BooleanField(required=False, label="Gerente de Cardápio")
    is_customer = forms.BooleanField(required=False, label="Cliente")


    first_name = forms.CharField(
        required=True,
        label=_("Nome"),
        max_length=50,
        widget=forms.TextInput(attrs={"id": "id_first_name", "class": "form-control"}),
    )

    last_name = forms.CharField(
        required=True,
        label=_("Sobrenome"),
        max_length=50,
        widget=forms.TextInput(attrs={"id": "id_last_name", "class": "form-control"}),
    )

    username = forms.CharField(
        required=True,
        label=_("Matrícula/Login"),
        max_length=10,  # Ajuste o tamanho de acordo com a necessidade
        widget=forms.TextInput(attrs={"id": "id_matricula", "class": "form-control"}),
    )

    email = forms.EmailField(
        required=True,
        label=_("E-mail Institucional"),
        max_length=254,
        #validators=[validate_email],
        #error_messages={"invalid": "Insira um e-mail válido"},
        widget=forms.EmailInput(attrs={"id": "id_email", "class": "form-control"}),
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={"id": "id_password1", "class": "form-control"}), # Widget de senha
            'password2': forms.PasswordInput(attrs={"id": "id_password2", "class": "form-control"}), # Widget de confirmação de senha
        }
   
    def save(self, commit=True): # Função para salvar o formulario:
       user = super().save(commit=False)  # Salva parcialmente o objeto User
       user.email = self.cleaned_data['email']  # Captura o e-mail
       user.first_name = self.cleaned_data['first_name']  # Captura o primeiro nome
       user.last_name = self.cleaned_data['last_name']  # Captura o sobrenome (separado)

        # Defina valores padrão ou deixe para o admin definir
       user.is_menu_manager = False  # Padrão: não é gerente de cardápio
       user.is_customer = True       # Padrão: é cliente      

      
       if commit: # Se commit=True, salva no banco de dados
            user.save()
       return user # Retorna o objeto User
    
    def clean_username(self): # Validação de cadastros Únicos
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Esta matricula já está cadastrada.")
        return username
    
    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email
