from django.contrib.auth.views import LoginView
from app_accounts.forms import LoginForm

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'