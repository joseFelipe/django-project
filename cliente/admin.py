from django.contrib import admin
from .models import Categoria, Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone', 'email', 'data_criacao', 'categoria']
    list_display_links = ['id', 'nome']
    list_editable = ['telefone', 'categoria']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)