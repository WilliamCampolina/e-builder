from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def minhas_obras(request):
    return render(request, 'em-construcao.html')

def meus_orcamentos(request):
    return render(request, 'em-construcao.html')

def relatorios(request):
    return render(request, 'em-construcao.html')

def perfil(request):
    return render(request, 'index.html')

def nopermissions(request):
    return render(request, 'no-permission.html')

