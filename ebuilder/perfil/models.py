from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Topicos(models.Model):
    descricao = models.CharField('Tópicos', max_length=255)

    def __str__(self):
        return self.descricao

class SubTopicos(models.Model):
    subtopicos = models.ForeignKey(Topicos, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.CharField('Subtópicos', max_length=255)

    def __str__(self):
        return self.descricao


class PerfilEmpresa(models.Model):
    #topico = models.ForeignKey(Topicos, on_delete=models.CASCADE)
    topicos = models.ManyToManyField(Topicos)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    razaoSocial = models.CharField('Razão Social', max_length=100)
    nome = models.CharField('Nome Fantasia', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    email = models.EmailField('Email')
    rua = models.CharField('Rua', max_length=100)
    cep = models.CharField('CEP', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    pais = models.CharField('Pais', max_length=100)

    def __str__(self):
        return self.nome


class PerfilProfissional(models.Model):
    #subtopico = models.ForeignKey(SubTopicos, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(SubTopicos)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    email = models.EmailField('Email')
    rua = models.CharField('Rua', max_length=100)
    cep = models.CharField('CEP', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    pais = models.CharField('Pais', max_length=100)

    def __str__(self):
        return self.nome