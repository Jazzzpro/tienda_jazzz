from django.contrib import admin
from .models import Producto, Nota


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    list_filter = ('categoria', 'stock')
    search_fields = ('nombre',)


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('autor', 'producto', 'puntuacion')