from django import forms
from django.contrib.auth.hashers import make_password
from app_EPINav.models import Colaborador

class ColaboradorForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    data_admissao = forms.DateField(
        input_formats=['%d-%m-%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Colaborador
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'data_admissao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        colaborador = super().save(commit=False)
        senha = self.cleaned_data.get("senha")
        if senha:
            colaborador.senha = make_password(senha)
        if commit:
            colaborador.save()
        return colaborador
