from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='inicio'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),
    path('categorias/<int:id>/', views.libros_por_categoria, name='libros_por_categoria'),
    path('base/', views.base, name='base'),
]