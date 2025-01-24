from django.shortcuts import render, redirect
from Usuarios.forms import CadastroForm

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save() # Salva no banco caso tudo esteja certo
            return redirect("sucesso")
    else:
        form = CadastroForm()

    return  render( request,"Usuarios/cadastro.html", {"form":form})
