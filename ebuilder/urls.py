
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ebuilder.core.urls')),
    path('contas/', include('ebuilder.contas.urls')),
    path('usuarios/', include('ebuilder.usuarios.urls')),
    path('perfil/', include('ebuilder.perfil.urls')),
    path('admin/', admin.site.urls),
]
