from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]