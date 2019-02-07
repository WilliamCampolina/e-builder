from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from ebuilder.contas.models import TipoConta, Conta
from ebuilder.contas.forms import ContaForm



# Create your views here.
@login_required
#@permission_required('ebuilder.list', login_url='nopermissions')
def list(request):
    tipoContas = TipoConta.objects.all()
    contas = Conta.objects.all()

    return render(request, 'contas/list.html', {'contas': contas, 'tipoContas': tipoContas})

@login_required
#@permission_required('ebuilder.cadastro', login_url='nopermissions')
def cadastro(request):
    form = ContaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'contas/cadastro.html', {'form': form})

@login_required
#@permission_required('ebuilder.atualizar', login_url='nopermissions')
def atualizar(request, id):
    conta = Conta.objects.get(id=id)
    form = ContaForm(request.POST or None, instance=conta)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'contas/cadastro.html', {'form': form, 'conta': conta})

@login_required
def apagar(request, id):
    conta = Conta.objects.get(id=id)

    if request.method == 'POST':
        conta.delete()
        return redirect(list)

    return render(request, 'contas/delete.html', {'conta': conta})
