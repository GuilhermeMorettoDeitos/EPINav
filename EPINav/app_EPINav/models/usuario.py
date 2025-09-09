from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UsuarioSistema(models.Model):
    nome_usuario = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)

    def set_password(self, raw_password):
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)

