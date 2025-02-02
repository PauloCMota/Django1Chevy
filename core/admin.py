from django.contrib import admin
from .models import Cliente, Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque')
admin.site.register(Produto , ProdutoAdmin)
admin.site.register(Cliente)