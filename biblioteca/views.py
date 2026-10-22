from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Categoria
from .forms import LibroForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class LibroListView(ListView):
    model = Libro
    template_name = 'templates_con_ia/lista_libros.html'
    context_object_name = 'libros'

    def get_queryset(self):
        queryset = Libro.objects.select_related('categoria').all()
        # Aquí puedes aplicar filtros adicionales si es necesario
        cat_id = self.request.GET.get('categoria')
        if cat_id:
            queryset = queryset.filter(categoria_id=cat_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['total_libros'] = self.get_queryset().count()
        context['disponibles'] = [libro for libro in self.get_queryset() if libro.disponible]
        return context

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'templates_con_ia/detalle_libro.html'
    context_object_name = 'libro'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'templates_con_ia/agregar_libro.html'
    success_url = '/lista_libros/'

    def form_valid(self, form):
        return super().form_valid(form)

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'templates_con_ia/editar_libro.html'
    success_url = '/lista_libros/'

    def form_valid(self, form):
        return super().form_valid(form)

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'templates_con_ia/eliminar_libro.html'
    success_url = '/lista_libros/'

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
