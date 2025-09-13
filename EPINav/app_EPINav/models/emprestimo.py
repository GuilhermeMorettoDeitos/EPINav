from django.db import models
from app_EPINav.models.colaborador import Colaborador

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Empréstimo #{self.id} - {self.colaborador.nome}"
