from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app_EPINav.models.colaborador import Colaborador
from app_EPINav.forms.colaborador import ColaboradorForm  # import do form específico

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'app_EPINav/pages/colaborador/colaborador_list.html'

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'app_EPINav/pages/colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'app_EPINav/pages/colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'app_EPINav/pages/colaborador/colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')
