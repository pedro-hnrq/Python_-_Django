from django.contrib import admin
from django.db import models
from django.db.models.query_utils import select_related_descend
from .models import Pessoa, Cargos, Pedido

class PedidoInline(admin.TabularInline):
    list_display = ('nome', 'quantidade', 'descricao')
    model = Pedido 
    extra = 0

# @admin.register(Pessoa)
# class PessoaAdmin(admin.ModelAdmin):
#     #Amostra as informações
#     list_display = ('nome', 'email', 'semha')
#     #Somente Leitura
#     readonly_fields = ('senha',)
#     #Barra de Pesquisa e definer por que buscar
#     search_fields =('nome',)
#     #Filta
#     list_filter = ('cargo',)
#     #Edita na Amostra
#     list_editable = ('email',)



admin.site.register(Cargos)



