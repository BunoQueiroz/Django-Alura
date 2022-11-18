from django.shortcuts import render, get_object_or_404, get_list_or_404
from pratos.models import Prato

def index(request):
    pratos = Prato.objects.order_by('-data_criacao').filter(publicada=True)

    dados = {
        'pratos': pratos
    }

    return render(request, 'pratos/index.html', dados)

def pratos(request, pratos_id):
    prato = get_object_or_404(Prato, pk=pratos_id)
    
    prato_a_exibir = {
        'prato': prato
    }
    
    return render(request, 'pratos/pratos.html', prato_a_exibir)

def cria_prato(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            nome = request.POST['nome_prato']
            prato_principal = request.POST['principal']
            acompanhamento = request.POST['acompanhamento']
            tempo_preparo = request.POST['tempo_preparo']
            serve_ate = request.POST['serve_ate']
            categoria = request.POST['categoria']
            foto = request.FILES['foto_prato']

            data = [nome, prato_principal, acompanhamento, tempo_preparo, serve_ate, categoria]

            if isEmpty(data):
                print('Há campo(s) vazio(s)')
            else:
                user = get_object_or_404(User, pk=request.user.id)
                prato = Prato.objects.create(pessoa=user, nome_prato=nome, principal=prato_principal, acompanhamento=acompanhamento, tempo_medio_preparo=tempo_preparo, serve_ate=serve_ate, categoria=categoria, foto_prato=foto)
                prato.save()
            return redirect('dashboard')

        return render(request, 'pratos/cria_prato.html')
    return redirect('index')
    
def edita_prato(request, prato_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            prato_id = request.POST['prato_id']

            p = Prato.objects.get(pk=prato_id)

            p.nome_prato = request.POST['nome_prato']
            p.principal = request.POST['principal']
            p.acompanhamento = request.POST['acompanhamento']
            p.tempo_preparo = request.POST['tempo_preparo']
            p.serve_ate = request.POST['serve_ate']
            p.categoria = request.POST['categoria']
            
            if 'foto_prato' in request.FILES:
                p.foto_prato = request.FILES['foto_prato']
            p.save()
            messages.success(request, 'Deu certo')
            return redirect('dashboard')

        prato = get_object_or_404(klass=Prato, pk=prato_id)
        data = {
            'prato': prato
        }
        return render(request, 'pratos/editar_prato.html', data)
    messages.error(request, 'Você não tem permissão de acesso sem estar logado')
    return redirect('index')

def deleta_prato(request, prato_id):
    if request.user.is_authenticated:
        prato = get_object_or_404(Prato, pk=prato_id)
        prato.delete()
        messages.success(request, 'Prato deletado com sucesso')
        return redirect('dashboard')
    messages.error(request, 'você não tem permissão de acesso à página requisitada')
    return redirect('index')
