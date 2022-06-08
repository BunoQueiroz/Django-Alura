from django.contrib import admin
from .models import Prato

class ListaPratos(admin.ModelAdmin):
    list_display = ('id', 'nome_prato', 'categoria')
    list_display_links = ('id', 'nome_prato')
    search_fields = ('nome_prato',)
    list_filter = ('categoria',)
    list_per_page = 5

admin.site.register(Prato, ListaPratos)