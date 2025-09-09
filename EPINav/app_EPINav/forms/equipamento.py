from django import forms
from app_EPINav.models.equipamento import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao', 'fabricante', 'estado']
