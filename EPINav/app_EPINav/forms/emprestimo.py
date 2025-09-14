from django import forms
from app_EPINav.models.emprestimo import Emprestimo
from django.utils import timezone

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        # Removendo 'observacao' se não existir
        fields = ['equipamento', 'data_prevista_devolucao']
        widgets = {
            'data_prevista_devolucao': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
        }

    def clean_data_prevista_devolucao(self):
        data = self.cleaned_data.get('data_prevista_devolucao')
        from django.utils import timezone
        if data and data <= timezone.now():
            raise forms.ValidationError(
                "A data prevista para devolução deve ser posterior à data e hora atual."
            )
        return data
