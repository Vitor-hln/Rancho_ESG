
# FBV (Funciton Bsed View)
"""from django.shortcuts import render, redirect

from  Usuarios.forms import CadastroForm

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save() # Salva no banco caso tudo esteja certo
            return redirect("sucesso")
    else:
        # Formulario vazio para tratar GET
        form = CadastroForm()

    return  render( request,"Usuarios/cadastro.html", {"form":form})
"""
#------------------------------------------------------------------------------------------#

# CBV (Class based view)

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from Usuarios.forms import CadastroForm
from Usuarios.models import Usuario

# CBV (Class Based View ou View Baseada em Classe)
class UsuarioView(CreateView):
    model = Usuario # O Model a ser usado
    form_class = CadastroForm # O Form correspondente
    template_name = 'cadastro.html' # O Template que será renderizado
    success_url = reverse_lazy('criar_produto_2') # Url de redirecionamento após salvar

