# -- TESTE UNITÁRIO 03 --

import pytest
from app_EPINav.models.colaborador import Colaborador

# Realizar login como Colaborador (colaborador) corretamente.

@pytest.mark.django_db
def test_login_colaborador_simulado(client):
    # cria colaborador
    colaborador = Colaborador.objects.create(
        nome="Colaborador Teste",
        cargo="Técnico",
        nome_usuario="colaborador1",
        senha="senha123"
    )
    colaborador.set_password("senha123")
    colaborador.save()

    # login na sessão
    session = client.session
    session['usuario_id'] = colaborador.id
    session['tipo_usuario'] = 'colaborador'
    session.save()

    # verifica se a sessão foi criada corretamente
    assert client.session.get('usuario_id') == colaborador.id
    assert client.session.get('tipo_usuario') == 'colaborador'
