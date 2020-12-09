from django.shortcuts import render

def lista_produto(request):
    return render(request, 'marketdb/lista_produto.html', {})