from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def isEmpty(list_itens):
    for i in list_itens:
        if i.strip() == '':
            return True
        else:
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
            user = User.objects.create(is_superuser=False, username=name, email=email, password=password)
            user.save()
            
            print(data)
            return redirect('login')
    else:
        return render(request, 'users/registration.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, template_name)

def dashboard(request):
    return render(request, template_name)