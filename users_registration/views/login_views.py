from django.contrib.auth.views import LoginView
from users_registration.forms import LoginForm

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'