# python já vem com um sistema de registro de usuarios embutido aqui vou tentar utilizar o mesmo
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

"""class RegistrationForm(UserCreationForm):
    nome = forms.CharField(max_length=100, label="Nome")
    matricula = forms.CharField(max_length=10, min_length=10, label="Matricula")
    email = forms.EmailField(required=True, label='E-amil Institucional', max_length = 254, validators=[validate_email], error_messages={'invalid': 'Insira um e-mail válido'})

class Meta:
    model = User
    fields = ['username','password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['nome']  # Salvando o nome no campo first_name
        user.matricula = self.cleaned_data.get('matricula')  # Salvando a matrícula
        if commit:
            user.save()

        return user"""


class RegistrationForm(UserCreationForm):
    nome = forms.CharField(
        max_length=100,
        label="Nome",
        widget=forms.TextInput(attrs={"id": "id_nome", "class": "form-control"}),
    )
    matricula = forms.CharField(
        max_length=10,
        min_length=10,
        label="Matrícula",
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
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"id": "id_username", "class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"id": "id_password1", "class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"id": "id_password2", "class": "form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['nome']  # Salvando o nome no campo first_name

        # Salvar matrícula como um atributo customizado em outro modelo ou banco de dados
        matricula = self.cleaned_data.get('matricula')  # Recuperando a matrícula
        # Aqui, você pode salvar em outro modelo ou processá-la

        if commit:
            user.save()

        return user
