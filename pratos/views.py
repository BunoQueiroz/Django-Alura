from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pratos(request):
    return render(request, 'pratos.html')