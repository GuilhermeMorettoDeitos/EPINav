from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Ativo")
    data_admissao = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
