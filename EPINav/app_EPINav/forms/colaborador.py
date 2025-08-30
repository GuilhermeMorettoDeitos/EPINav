from django import forms
from app_EPINav.models import Colaborador

class ColaboradorForm(forms.ModelForm):
    data_admissao = forms.DateField(
    input_formats=['%d-%m-%Y', '%Y-%m-%d'],
    widget=forms.DateInput(attrs={'type': 'date'})
)

    class Meta:
        model = Colaborador
        fields = '__all__'