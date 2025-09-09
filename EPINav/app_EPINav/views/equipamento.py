from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app_EPINav.models.equipamento import Equipamento
from app_EPINav.forms.equipamento import EquipamentoForm

class EquipamentoListView(ListView):
    model = Equipamento
    template_name = 'app_EPINav/pages/equipamento/equipamento_list.html'
    context_object_name = 'equipamentos'


class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'app_EPINav/pages/equipamento/equipamento_form.html'
    success_url = reverse_lazy('equipamento_list')


class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'app_EPINav/pages/equipamento/equipamento_form.html'
    success_url = reverse_lazy('equipamento_list')


class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    template_name = 'app_EPINav/pages/equipamento/equipamento_confirm_delete.html'
    success_url = reverse_lazy('equipamento_list')
