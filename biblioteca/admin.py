from django.contrib import admin
from .models import Libro, Categoria



@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor',)
    search_fields = ('titulo', 'autor')
    list_filter = ('disponible',)

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 1
    fields = ['isbn','titulo','autor','precio_prestamo','disponible', 'stock_copias']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','total_libros_asociados')
    search_fields = ('nombre',)
    inlines = [LibroInline]

    @admin.display(description="Total de Libros")
    def total_libros_asociados(self, obj):
        return obj.libros.count()


