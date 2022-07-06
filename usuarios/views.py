from django.shortcuts import render

def registration(request):
    return render(request, template_name)

def login(request):
    return render(request, template_name)

def logout(request):
    return render(request, template_name)

def dashboard(request):
    return render(request, template_name)