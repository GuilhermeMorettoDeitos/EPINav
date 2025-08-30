from django.shortcuts import render, redirect
from django.contrib import messages
from app_EPINav.models.usuario import UsuarioSistema

def login_view(request):
    if request.method == "POST":
        nome_usuario = request.POST.get("nome_usuario")
        senha = request.POST.get("senha")

        try:
            user = UsuarioSistema.objects.get(nome_usuario=nome_usuario)
            if user.check_password(senha):
                request.session["usuario_id"] = user.id
                request.session["is_admin"] = user.is_admin
                return redirect("home")
            else:
                messages.error(request, "Senha incorreta.")
        except UsuarioSistema.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")

    return render(request, "app_EPINav/pages/login.html")
