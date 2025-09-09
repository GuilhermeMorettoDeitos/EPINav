from django import forms
from app_EPINav.models.usuario import UsuarioSistema

class UsuarioSistemaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = UsuarioSistema
        fields = ["nome_usuario", "senha", "is_admin"]

    def save(self, commit=True):
        usuario = super().save(commit=False)
        senha = self.cleaned_data.get("senha")
        if senha:
            usuario.set_password(senha)  # hash da senha
        if commit:
            usuario.save()
        return usuario
