from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from pratos.models import Prato

def isEmpty(list_itens):
    for i in list_itens:
        if i.strip() == '':
            return True
    return False

def registration(request):
    if request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        data = [name, email, password, password2]

        if isEmpty(data) or password != password2 or User.objects.filter(email=email).exists():
            messages.error(request, 'Não podem haver campos vazios!')
            return render(request, 'users/registration.html')
        else:
            user = User.objects.create_user(is_superuser=False, username=name, email=email, password=password)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')
    else:
        return render(request, 'users/registration.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = [email, password]
        if isEmpty(data) or User.objects.filter(email=email, password=password).exists():
            return render(request, 'users/login.html')
        else:
            name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        prato = Prato.objects.order_by('-id').filter(pessoa_id=id)
        data = {
            'pratos' : prato
        }

        return render(request, 'users/dashboard.html', data)
    else:
        return redirect('index')

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

        return render(request, 'users/cria_prato.html')
    else:
        return redirect('index')
    
