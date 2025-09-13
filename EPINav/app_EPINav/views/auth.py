from django.shortcuts import render, redirect
from django.contrib import messages
from app_EPINav.models.usuario import UsuarioSistema
from app_EPINav.models import Colaborador

def login_view(request):
    if request.method == "POST":
        nome_usuario = request.POST.get("nome_usuario")
        senha = request.POST.get("senha")

        user = None

        # Tenta buscar primeiro UsuarioSistema
        try:
            user = UsuarioSistema.objects.get(nome_usuario=nome_usuario)
            if user.check_password(senha):
                request.session['usuario_id'] = user.id
                request.session['nome_usuario'] = user.nome_usuario
                request.session['is_admin'] = user.is_admin
                request.session['tipo_usuario'] = 'sistema'
            else:
                user = None
        except UsuarioSistema.DoesNotExist:
            pass

        # Se não encontrou, tenta Colaborador
        if user is None:
            try:
                user = Colaborador.objects.get(nome_usuario=nome_usuario)
                if user.check_password(senha):
                    request.session['usuario_id'] = user.id
                    request.session['nome_usuario'] = user.nome_usuario
                    request.session['tipo_usuario'] = 'colaborador'
                else:
                    user = None
            except Colaborador.DoesNotExist:
                user = None

        if user:
            next_url = request.POST.get('next') or 'home'
            return redirect(next_url)
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "app_EPINav/pages/login.html")


def logout_view(request):
    request.session.flush()
    messages.success(request, "Você saiu do sistema.")
    return redirect("login")
