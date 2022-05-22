from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Vai dar certo, você consegue</h1>')