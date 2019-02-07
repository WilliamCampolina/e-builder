
from django.urls import path
from ebuilder.perfil.views import cadastro_perfil_empresa, atualizar_empresa, list_perfil_empresa, \
    list_perfil_profissional, cadastro_perfil_profissional, atualizar_profissional

urlpatterns = [
    path('empresa', list_perfil_empresa, name='list_perfil_empresa'),
    path('profissional', list_perfil_profissional, name='list_perfil_profissional'),
    path('novoEmpresa', cadastro_perfil_empresa, name='cadastro_perfil_empresa'),
    path('novoProfissional', cadastro_perfil_profissional, name='cadastro_perfil_profissional'),
    # path('update/<int:id>/', atualizar, name='atualizar'),
    path('atualizarEmpresa/<int:id>/', atualizar_empresa, name='atualizar_empresa'),
    path('atualizarProfissional/<int:id>/', atualizar_profissional, name='atualizar_profissional'),
    # path('apagar/<int:id>/', apagar, name='apagar')

]
