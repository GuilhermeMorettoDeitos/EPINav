from django import forms
from django.contrib.auth.hashers import make_password
from app_EPINav.models import Colaborador

class ColaboradorForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    data_admissao = forms.DateField(
        input_formats=['%d-%m-%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Colaborador
        fields = '__all__'

    def save(self, commit=True):
        colaborador = super().save(commit=False)
        senha = self.cleaned_data.get("senha")
        if senha:
            colaborador.senha = make_password(senha)
        if commit:
            colaborador.save()
        return colaborador
