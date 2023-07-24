from django.db import models


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    email = models.EmailField('Email', max_length=50)
    cpf = models.CharField('CPF', max_length=12)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Carro(models.Model):
    carro = models.CharField('Carro', max_length=50)
    placa = models.CharField('Placa', max_length=50)
    ano = models.IntegerField('Ano')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self):
        return self.carro
