from django.contrib import admin

# Register your models here.
from ebuilder.perfil.models import Topicos, SubTopicos, PerfilEmpresa, PerfilProfissional

admin.site.register(Topicos)
admin.site.register(SubTopicos)
admin.site.register(PerfilEmpresa)
admin.site.register(PerfilProfissional)