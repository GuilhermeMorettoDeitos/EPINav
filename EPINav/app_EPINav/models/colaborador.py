from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Ativo")
    data_admissao = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    nome_usuario = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)
    foto = models.ImageField(upload_to="colaboradores/", blank=True, null=True)


    def set_password(self, raw_password):
        self.senha = make_password(raw_password)
        self.save(update_fields=['senha'])

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)

    def __str__(self):
        return self.nome
