from django.urls import path, include
from ebuilder.core.views import home, index, meus_orcamentos, perfil, minhas_obras, relatorios, nopermissions


urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('orcamentos', meus_orcamentos, name='orcamentos'),
    path('perfil', perfil, name='perfil'),
    path('obras', minhas_obras, name='obras'),
    path('relatorios', relatorios, name='relatorios'),
    path('nopermissions', nopermissions, name='nopermissions')

]
