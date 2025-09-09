from django.db import models

class Equipamento(models.Model):
    ESTADOS = [
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('manutencao', 'Em manutenção'),
        ('inativo', 'Inativo'),
    ]

    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True, null=True)
    fabricante = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='novo')

    def __str__(self):
        return f"{self.nome} - {self.fabricante}"
