from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:pratos_id>', pratos, name='pratos'),
    path('search', search, name='search'),
    path('cria_prato', cria_prato, name='cria_prato'),
    path('edita_prato/<int:prato_id>', edita_prato, name='edita_prato'),
    path('deleta_prato/<int:prato_id>', deleta_prato, name='deleta_prato'),
]
