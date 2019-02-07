from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from ebuilder.contas.models import Conta, TipoConta
from ebuilder.perfil.forms import PerfilEmpresaForm, PerfilProfissionalForm
from ebuilder.perfil.models import PerfilEmpresa, PerfilProfissional


def list_perfil_empresa(request):
    current_user = request.user
    empresa = PerfilEmpresa.objects.filter(id=current_user.id)
    #print(empresa)
    if empresa:
        empresa = empresa.get()

    return render(request, 'perfil-empresa.html', {'empresa': empresa})

@login_required
def cadastro_perfil_empresa(request):

    form = PerfilEmpresaForm(request.POST or None)
    form.usuario = request.user
    if form.is_valid():
        form.save()
        return redirect('list_perfil_empresa')

    return render(request, 'nova-empresa.html', {'form': form})


@login_required
def atualizar_empresa(request, id):
    empresa = PerfilEmpresa.objects.get(id=id)
    form = PerfilEmpresaForm(request.POST or None, instance=empresa)

    if form.is_valid():
        form.save()
        return redirect('list_perfil_empresa')

    return render(request, 'nova-empresa.html', {'form': form, 'empresa': empresa})




def list_perfil_profissional(request):
    current_user = request.user
    profissional = PerfilProfissional.objects.filter(id=current_user.id)
    #print(profissional)
    if profissional:
        profissional = profissional.get()

    return render(request, 'perfil-profissional.html', {'profissional': profissional})


@login_required
def cadastro_perfil_profissional(request):

    form = PerfilProfissionalForm(request.POST or None)
    form.usuario = request.user


    if form.is_valid():
        form.save()
        return redirect('list_perfil_profissional')


    return render(request, 'novo-profissional.html', {'form': form})


@login_required
def atualizar_profissional(request, id):

    profissional = PerfilProfissional.objects.get(id=id)
    form = PerfilProfissionalForm(request.POST or None, instance=profissional)

    if form.is_valid():
        form.save()
        return redirect('list_perfil_profissional')

    return render(request, 'novo-profissional.html', {'form': form, 'profissional': profissional})




