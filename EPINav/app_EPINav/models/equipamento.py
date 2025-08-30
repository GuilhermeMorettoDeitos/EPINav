from django.db import models

# Create your models here.

class equipamentos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    fabricante = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nome