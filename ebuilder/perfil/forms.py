from django import forms

from ebuilder.perfil.models import PerfilEmpresa, PerfilProfissional


class PerfilEmpresaForm(forms.ModelForm):
    class Meta:
        model = PerfilEmpresa
        fields = ['topicos', 'razaoSocial', 'nome', 'telefone', 'email', 'rua', 'cep', 'cidade', 'estado', 'pais']

class PerfilProfissionalForm(forms.ModelForm):
    class Meta:
        model = PerfilProfissional
        fields = ['servicos', 'nome', 'sobrenome', 'telefone', 'email', 'rua', 'cep', 'cidade', 'estado', 'pais']