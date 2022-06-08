from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Prato

def index(request):
    pratos = Prato.objects.all()

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