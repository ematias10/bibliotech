from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.lista_libros, name='inicio'),
    path('libros/', views.LibroListView.as_view(), name='lista_libros'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='detalle_libro'),
    path('libros/agregar/', views.LibroCreateView.as_view(), name='agregar_libro'),
    path('categorias/<int:id>/', views.libros_por_categoria, name='libros_por_categoria'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='eliminar_libro'),
    path('base/', views.base, name='base'),
]