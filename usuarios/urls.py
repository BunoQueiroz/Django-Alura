from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria_prato', views.cria_prato, name='cria_prato'),
    path('edita_prato/<int:prato_id>', views.edita_prato, name='edita_prato'),
]