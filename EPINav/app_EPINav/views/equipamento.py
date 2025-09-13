from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from app_EPINav.models.equipamento import Equipamento
from app_EPINav.forms.equipamento import EquipamentoForm
from app_EPINav.views.decorators import login_required_custom

# Listagem de equipamentos (apenas usuários logados podem acessar)
@method_decorator(login_required_custom, name="dispatch")
class EquipamentoListView(ListView):
    model = Equipamento
    template_name = 'app_EPINav/pages/equipamento/equipamento_list.html'
    context_object_name = 'equipamentos'


# Criação de equipamentos
@method_decorator(login_required_custom, name="dispatch")
class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'app_EPINav/pages/equipamento/equipamento_form.html'
    success_url = reverse_lazy('equipamento_list')


# Atualização de equipamentos
@method_decorator(login_required_custom, name="dispatch")
class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'app_EPINav/pages/equipamento/equipamento_form.html'
    success_url = reverse_lazy('equipamento_list')


# Exclusão de equipamentos (ainda usando modal no front-end)
@method_decorator(login_required_custom, name="dispatch")
class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    success_url = reverse_lazy('equipamento_list')
