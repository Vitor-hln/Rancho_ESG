from django import forms
from django.core.exceptions import ValidationError

from app_accounts.models import CustomUser
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
def validate_username(value):
    if not value.isdigit():
        raise ValidationError("Este campo deve conter apenas números.")


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
        max_length=10,
        widget=forms.TextInput(attrs={"id": "id_matricula", "class": "form-control"}),
        validators=[validate_username]
    )

    email = forms.EmailField(
        required=True,
        label=_("E-mail Institucional"),
        max_length=254,
        widget=forms.EmailInput(attrs={"id": "id_email", "class": "form-control"}),
    )

    class Meta:
        model = CustomUser  # Use o modelo CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={"id": "id_password1", "class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"id": "id_password2", "class": "form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_menu_manager = self.cleaned_data['is_menu_manager']
        user.is_customer = self.cleaned_data['is_customer']

        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Esta matrícula já está cadastrada.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email