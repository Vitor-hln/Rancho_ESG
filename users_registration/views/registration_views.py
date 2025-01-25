from django.shortcuts import render, redirect
from django.contrib import messages
from users_registration.forms import RegistrationForm

def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso. /n Você será redirecionado para a página de login!")
            return redirect("login.html") # Nome da URL de LOGIN

    else:
        form=RegistrationForm()

    return render(request, 'registro.html', {'form':form})