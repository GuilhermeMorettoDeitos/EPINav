from django import forms
from django.utils import timezone
from app_EPINav.models.equipamento import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao', 'fabricante', 'estado', 'data_devolucao', 'observacao_devolucao']
        widgets = {
            'data_devolucao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observacao_devolucao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se for criação (sem instância existente), filtra os estados
        if not self.instance or not self.instance.pk:
            allowed_choices = [
                ('emprestado', 'Emprestado'),
                ('em_uso', 'Em uso'),
                ('fornecido', 'Fornecido'),
            ]
            self.fields['estado'].choices = allowed_choices

    def clean_data_devolucao(self):
        data = self.cleaned_data.get('data_devolucao')
        if data and data < timezone.now().date():
            raise forms.ValidationError("A data prevista para devolução deve ser posterior à data atual.")
        return data
