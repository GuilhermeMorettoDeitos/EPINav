from django.contrib.auth.views import LoginView
from app_EPINav.forms.usuarioSistema import FormularioLogin

class FormularioLogin(LoginView):
    template_name = 'app_EPINav/pages/login.html'
    authentication_form = FormularioLogin 