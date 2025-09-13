from django.shortcuts import render, redirect, get_object_or_404
from app_EPINav.models.emprestimo import Emprestimo
from app_EPINav.models.emprestimo_item import EmprestimoItem
from app_EPINav.forms.emprestimo_item import EmprestimoItemForm

def emprestimo_detail(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    itens = emprestimo.itens.all()  # pega todos os itens do empréstimo

    # Para adicionar um novo item
    if request.method == 'POST' and 'add_item' in request.POST:
        form = EmprestimoItemForm(request.POST)
        if form.is_valid():
            novo_item = form.save(commit=False)
            novo_item.emprestimo = emprestimo
            novo_item.save()
            return redirect('emprestimo_detail', pk=pk)
    else:
        form = EmprestimoItemForm()

def emprestimoitem_update(request, pk):
    item = get_object_or_404(EmprestimoItem, pk=pk)
    if request.method == 'POST':
        form = EmprestimoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_detail', pk=item.emprestimo.pk)
    else:
        form = EmprestimoItemForm(instance=item)
    return render(request, 'app_EPINav/pages/emprestimo/emprestimoitem_form.html', {'form': form})

    return render(request, 'app_EPINav/pages/emprestimo/emprestimo_detail.html', {
        'emprestimo': emprestimo,
        'itens': itens,
        'form': form,
        
        
    })
    
    
