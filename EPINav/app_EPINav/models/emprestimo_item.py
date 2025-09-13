from django.db import models
from app_EPINav.models.emprestimo import Emprestimo
from app_EPINav.models.equipamento import Equipamento

class EmprestimoItem(models.Model):
    STATUS_CHOICES = [
        ("EMPRESTADO", "Emprestado"),
        ("EM_USO", "Em Uso"),
        ("FORNECIDO", "Fornecido"),
        ("DEVOLVIDO", "Devolvido"),
        ("DANIFICADO", "Danificado"),
        ("PERDIDO", "Perdido"),
    ]

    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, related_name="itens")
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="EMPRESTADO")
    data_devolucao = models.DateField(null=True, blank=True)
    observacao_devolucao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipamento.nome} ({self.get_status_display()})"
