from django.db import models
from django.utils import timezone
from django.conf import settings
from djmoney.models.fields import MoneyField

class Produto(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dataCriacao = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    preco = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='BRL',
        max_digits=6,
    )
    imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='SEM IMAGEM')


    def cadastrar(self):
        self.dataCriacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

