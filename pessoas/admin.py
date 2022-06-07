from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cargo')
    list_display_links = ('id', 'nome')
    list_filter = ('cargo',)

admin.site.register(Pessoa, ListandoPessoas)