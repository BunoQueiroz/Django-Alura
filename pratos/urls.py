from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pratos_id>', views.pratos, name='pratos'),
    path('buscar', views.buscar, name='buscar')
]
