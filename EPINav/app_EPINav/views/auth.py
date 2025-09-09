from django.shortcuts import render, redirect
from django.contrib import messages
from app_EPINav.models.usuario import UsuarioSistema


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
                request.session['usuario_id'] = user.id
                request.session['nome_usuario'] = user.nome_usuario
                request.session['is_admin'] = user.is_admin
                request.session.modified = True

                # redireciona para o "next" se existir, senão para home
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, "Senha incorreta.")
        except UsuarioSistema.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")

    return render(request, "app_EPINav/pages/login.html")




def logout_view(request):
    request.session.flush()  # limpa a sessão inteira
    messages.success(request, "Você saiu do sistema.")
    return redirect("login")

