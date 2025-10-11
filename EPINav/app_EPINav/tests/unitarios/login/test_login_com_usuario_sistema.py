# -- TESTE UNITÁRIO 01 --

import pytest
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from app_EPINav.models.usuario import UsuarioSistema
from django.contrib.messages import get_messages


#Testa se o usuário do sistema consegue fazer login com credenciais válidas.
@pytest.mark.django_db
def test_usuario_sistema_pode_logar(client):    
    # cria um usuário
    usuario = UsuarioSistema.objects.create(
        nome_usuario="admin",
        is_admin=True,
    )
    usuario.set_password("123")
    usuario.save()

    # faz o login pela view de login (ajuste o nome da URL conforme seu projeto)
    response = client.post(
        reverse("login"),
        {"nome_usuario": "admin", "senha": "123"},
        follow=True
    )

    # verifica se login funcionou
    assert response.status_code == 200
    assert "sessionid" in response.client.cookies  # sessão criada
    assert response.wsgi_request.session.get("usuario_id") == usuario.id
    assert response.wsgi_request.session.get("is_admin") is True

