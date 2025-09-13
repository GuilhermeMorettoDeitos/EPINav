# app_EPINav/forms/emprestimo_item.py
from django import forms
from app_EPINav.models.emprestimo_item import EmprestimoItem

class EmprestimoItemForm(forms.ModelForm):
    class Meta:
        model = EmprestimoItem
        fields = ['equipamento', 'status', 'data_devolucao', 'observacao_devolucao']
