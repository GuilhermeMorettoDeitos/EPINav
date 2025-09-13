# app_EPINav/forms/emprestimo.py
from django import forms
from app_EPINav.models.emprestimo import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = []  # nenhum campo é necessário, já que o colaborador vem do login
