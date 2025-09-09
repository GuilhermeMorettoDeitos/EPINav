from django.contrib import admin
from django.urls import path

from app_EPINav.views import (
    ColaboradorListView,
    ColaboradorCreateView,
    ColaboradorUpdateView,
    ColaboradorDeleteView,
    home
)

from app_EPINav.views.usuarioSistema import (
    listar_usuarios, criar_usuario,
    editar_usuario, deletar_usuario
)

from app_EPINav.views.auth import login_view, logout_view

from app_EPINav.views.equipamento import (
    EquipamentoListView, EquipamentoCreateView,
    EquipamentoUpdateView, EquipamentoDeleteView
)

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),

    # Colaboradores
    path('colaboradores/', ColaboradorListView.as_view(), name='colaborador_list'),
    path('colaboradores/novo/', ColaboradorCreateView.as_view(), name='colaborador_create'),
    path('colaboradores/<int:pk>/editar/', ColaboradorUpdateView.as_view(), name='colaborador_update'),
    path('colaboradores/<int:pk>/deletar/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),

    # Usuários
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/novo/', criar_usuario, name='criar_usuario'),
    path('usuarios/<int:pk>/editar/', editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/deletar/', deletar_usuario, name='deletar_usuario'),
    
    # Equipamentos
    path('equipamentos/', EquipamentoListView.as_view(), name='equipamento_list'),
    path('equipamentos/novo/', EquipamentoCreateView.as_view(), name='equipamento_create'),
    path('equipamentos/<int:pk>/editar/', EquipamentoUpdateView.as_view(), name='equipamento_update'),
    path('equipamentos/<int:pk>/excluir/', EquipamentoDeleteView.as_view(), name='equipamento_delete'),
]
