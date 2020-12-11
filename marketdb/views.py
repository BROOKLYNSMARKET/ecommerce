from django.shortcuts import render

def lista_produto(request):
    tiago = 'iTiagod'
    return render(request, 'marketdb/lista_produto.html', {})