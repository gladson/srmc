# coding: utf-8
from srmc.app_srmc.models import *
from django.contrib import admin

class Cad_produtorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'rg']
    search_fields = ['nome', 'data_de_nascimento', 'cpf', 'rg', 'uf', 'municipio', 'cep', 'bairro', 'endereco', 'numero', 'complemento']
    list_filter = ['sexo', ]

admin.site.register(Cad_produtor, Cad_produtorAdmin)
admin.site.register(Cad_endereco_propriedade)
admin.site.register(Uso_solo)
admin.site.register(Uso_solo_unidade)
admin.site.register(Uso_agua)
admin.site.register(Criacao)
admin.site.register(Cad_uso)