from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email

# Utilizar após saber o dominio do e-mail utilizado na ESG
"""from django.core.exceptions import ValidationError    
from django.utils.translation import gettext_lazy as _

def validar_email_personalizado(value):
    if not value.endswith('@exemplo.com'):
        raise ValidationError(
            _('Somente e-mails do domínio @exemplo.com são permitidos.'),
            params={'value': value},
        )"""

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label="Nome",
        max_length=50,
        widget=forms.TextInput(attrs={"id": "id_first_name", "class": "form-control"}),
    )

    last_name = forms.CharField(
        required=True,
        label="Sobrenome",
        max_length=50,
        widget=forms.TextInput(attrs={"id": "id_last_name", "class": "form-control"}),
    )

    username = forms.CharField(
        required=True,
        label="Matrícula/Login",
        max_length=10,  # Ajuste o tamanho de acordo com a necessidade
        widget=forms.TextInput(attrs={"id": "id_matricula", "class": "form-control"}),
    )

    email = forms.EmailField(
        required=True,
        label="E-mail Institucional",
        max_length=254,
        validators=[validate_email],
        error_messages={"invalid": "Insira um e-mail válido"},
        widget=forms.EmailInput(attrs={"id": "id_email", "class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={"id": "id_password1", "class": "form-control"}), # Widget de senha
            'password2': forms.PasswordInput(attrs={"id": "id_password2", "class": "form-control"}), # Widget de confirmação de senha
        }


    # Função para salvar o formulario:
    def save(self, commit=True):
       user = super().save(commit=False)  # Salva parcialmente o objeto User
       user.email = self.cleaned_data['email']  # Captura o e-mail
       user.first_name = self.cleaned_data['first_name']  # Captura o primeiro nome
       user.last_name = self.cleaned_data['last_name']  # Captura o sobrenome (separado)
      
       if commit: # Se commit=True, salva no banco de dados
               user.save()
       return user # Retorna o objeto User
    
    
    # Validação de cadastros Únicos

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Esta matricula já está cadastrada.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email
