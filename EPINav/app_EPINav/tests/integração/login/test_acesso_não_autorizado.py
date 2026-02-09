
#  -- TESTE DE INTEGRAÇÃO 01 --

import pytest
from django.urls import reverse

# verificar se um usuário não logado tem acesso às páginas de funcionalidade do sistema (home, colaboradores, empréstimo, etc).

PROTECTED_URLS = [
    "home",
    "colaborador_list",
    "emprestimo_list",
    "equipamento_list",
    "relatorios",
]

@pytest.mark.django_db
@pytest.mark.parametrize("url_name", PROTECTED_URLS)
def test_usuario_nao_logado_redirecionado_para_login(client, url_name):
    url = reverse(url_name)
    response = client.get(url, follow=False)

    # verifica se redirecionou
    assert response.status_code in [301, 302], f"A URL '{url_name}' não redirecionou."

    login_url = reverse("login") 
    assert response.url.startswith(login_url), f"A URL '{url_name}' não redirecionou para login."
