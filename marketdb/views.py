from django.shortcuts import render
from .models import Produto, CategoriaProduto

def lista_produto(request):
    List = Produto.objects.all()
    return render(request, 'marketdb/lista_produto.html', {'List': List})