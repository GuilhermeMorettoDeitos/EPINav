from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from app_EPINav.models.colaborador import Colaborador
from app_EPINav.forms.colaborador import ColaboradorForm
from app_EPINav.views.decorators import login_required_custom, admin_required

# Listagem de colaboradores
@method_decorator([login_required_custom, admin_required], name='dispatch')
class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'app_EPINav/pages/colaborador/colaborador_list.html'
    context_object_name = 'colaboradores'


# Criação de colaboradores
@method_decorator([login_required_custom, admin_required], name='dispatch')
class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'app_EPINav/pages/colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')


# Atualização de colaboradores
@method_decorator([login_required_custom, admin_required], name='dispatch')
class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'app_EPINav/pages/colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')


# Exclusão de colaboradores
@method_decorator([login_required_custom, admin_required], name='dispatch')
class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('colaborador_list')
