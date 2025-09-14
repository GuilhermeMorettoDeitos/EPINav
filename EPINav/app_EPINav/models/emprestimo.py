from django.db import models
from django.utils import timezone
from app_EPINav.models.colaborador import Colaborador
from app_EPINav.models.equipamento import Equipamento

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ("emprestado", "Emprestado"),
        ("em_uso", "Em Uso"),
        ("fornecido", "Fornecido"),
        ("devolvido", "Devolvido"),
        ("danificado", "Danificado"),
        ("perdido", "Perdido"),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="emprestimos")
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name="emprestimos")
    data_entrega = models.DateTimeField(default=timezone.now)
    data_prevista_devolucao = models.DateTimeField()
    data_devolucao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="emprestado")
    observacao_devolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipamento.nome} - {self.colaborador.nome} ({self.get_status_display()})"
