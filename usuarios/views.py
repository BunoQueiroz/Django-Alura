from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
            return render(request, 'users/registration.html')
        else:
            user = User.objects.create_user(is_superuser=False, username=name, email=email, password=password)
            user.save()
            
            print(data)
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
    return render(request, template_name)

def dashboard(request):
    return render(request, 'users/dashboard.html')