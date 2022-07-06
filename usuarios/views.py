from django.shortcuts import render

def registration(request):
    return render(request, 'users/registration.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, template_name)

def dashboard(request):
    return render(request, template_name)