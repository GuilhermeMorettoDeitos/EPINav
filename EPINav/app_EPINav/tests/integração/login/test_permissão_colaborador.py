#  -- TESTE DE INTEGRAÇÃO 02 --

import pytest
from django.urls import reverse
from django.contrib.messages import get_messages
from app_EPINav.models.colaborador import Colaborador

# Testa que um colaborador não consegue acessar a lista de usuarios do sistema e é redirecionado para a home.

@pytest.mark.django_db
def test_colaborador_nao_pode_acessar_usuario_list(client):
    
    # Cria um colaborador
    colaborador = Colaborador.objects.create(
        nome="Colaborador Teste",
        cargo="Técnico",
        nome_usuario="colaborador1",
        senha="senha123"
    )

    # login do colaborador 
    session = client.session
    session['usuario_id'] = colaborador.id
    session['tipo_usuario'] = 'colaborador'
    session.save()

    #  tenta acessar a lista de usuários
    url = reverse("usuario_list")
    response = client.get(url, follow=True)

    # verifica redirecionamento para home
    assert response.status_code == 200
    assert response.redirect_chain[-1][0] == reverse("home")
    