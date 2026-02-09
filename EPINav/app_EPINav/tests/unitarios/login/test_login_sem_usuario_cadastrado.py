# -- TESTE UNITÁRIO 02 --

import pytest
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from app_EPINav.models.usuario import UsuarioSistema
from django.contrib.messages import get_messages

#Testa se o login falha quando a senha está incorreta.
@pytest.mark.django_db
def test_login_falha_com_senha_incorreta(client):
    # cria usuário
    usuario = UsuarioSistema.objects.create(
        nome_usuario="usuario_de_teste",
        is_admin=False
    )
    usuario.set_password("senha_certa")
    usuario.save()

    # tenta login com senha errada
    response = client.post(
        reverse("login"),
        {"nome_usuario": "usuario_de_teste", "senha": "senha_errada"},
        follow=True
    )

    # verifica se o usuário não foi autenticado
    assert response.status_code == 200
    assert response.wsgi_request.session.get("usuario_id") is None
    assert response.wsgi_request.session.get("is_admin") is None

    mensagens = list(get_messages(response.wsgi_request))
    assert any("usuário ou senha incorretos" in m.message.lower() for m in mensagens)