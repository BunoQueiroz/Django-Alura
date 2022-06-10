from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Prato

def index(request):
    pratos = Prato.objects.order_by('-data_criacao').filter(publicada=True)

    dados = {
        'pratos': pratos
    }

    return render(request, 'index.html', dados)

def pratos(request, pratos_id):
    prato = get_object_or_404(Prato, pk=pratos_id)
    prato_a_exibir = {
        'prato': prato
    }
    return render(request, 'pratos.html', prato_a_exibir)

def buscar(request):
    lista_pratos = Prato.objects.order_by('-id').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_pratos = lista_pratos.filter(nome_prato__icontains=nome_a_buscar)
    
    dados = {
        'pratos' : lista_pratos
    }

    return render(request, 'buscar.html', dados)