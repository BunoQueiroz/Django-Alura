from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from pratos.models import Prato

def is_empty(list_itens):
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

        if is_empty(data) or password != password2 or User.objects.filter(email=email).exists():
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
        if is_empty(data) or not User.objects.filter(email=email).exists():
            messages.error(request, 'Algo deu errado')
            return render(request, 'users/login.html')
        else:
            name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
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
    return redirect('index')
