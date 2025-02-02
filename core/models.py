from django.db import models
from django.db.models import DecimalField


# Create your models here.

class Produto(models.Model):
    nome = models.CharField('nome' , max_length=100)
    preco = models.DecimalField('preco' , decimal_places=2 , max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return f'{self.nome} {self.preco} {self.estoque}'


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.CharField('email',max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome} {self.email}'