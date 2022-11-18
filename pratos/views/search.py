from django.shortcuts import render
from pratos.models import Prato
from django.contrib import messages

def search(request): 
    if 'search' in request.GET:
        lista_pratos = Prato.objects.order_by('-id').filter(publicada=True)
        nome_a_buscar = request.GET['search'].strip()
        lista_pratos = lista_pratos.filter(nome_prato__icontains=nome_a_buscar)
        if lista_pratos.exists():
            dados = {
                'pratos' : lista_pratos
            }
            return render(request, 'pratos/search.html', dados)
        else:
            messages.error(request, 'Prato não encontrado')
            return render(request, 'pratos/search.html')
