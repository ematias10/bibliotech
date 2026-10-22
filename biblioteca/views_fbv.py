from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Categoria
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all().select_related('categoria')
    categorias = Categoria.objects.all()
    
    contexto = {
        'libros': libros,
        'disponibles': [libro for libro in libros if libro.disponible],
        'total_libros': libros.count(),
        'categorias': categorias,
    }

    return render(request, 'templates_con_ia/lista_libros.html', contexto)


def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    contexto = {
        'libro': libro
    }
    return render(request, 'templates_con_ia/detalle_libro.html', contexto)


def libros_por_categoria(request, id=None, cat=None):
    # Soporta tanto argumento 'id' como 'cat' para compatibilidad con urls
    cat_id = id if id is not None else cat
    categoria = get_object_or_404(Categoria, id=cat_id)
    libros = Libro.objects.filter(categoria=categoria).select_related('categoria')
    
    contexto = {
        'libros': libros,
        'categoria': categoria,
        'total_libros': libros.count()
    }
    return render(request, 'templates_con_ia/libros_por_categoria.html', contexto)

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()

    contexto = {
        'form': form
    }
    return render(request, 'templates_con_ia/agregar_libro.html', contexto)

def base(request):
    return render(request, 'templates_con_ia/base.html')