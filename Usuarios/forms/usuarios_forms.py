from django import forms
from  Usuarios.models import  Usuario

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'matricula', 'email'] # Campos exibidos no formulário

