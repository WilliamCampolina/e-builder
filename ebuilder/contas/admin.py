from django.contrib import admin
from ebuilder.contas.models import TipoConta, Conta

# Register your models here.
admin.site.register(TipoConta)
admin.site.register(Conta)