from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('', views.index, name="index"),
    # Crud de Categorias
    path('categorias_listar/', views.categorias, name="categorias_listar"),
    path('categorias_form/', views.categorias_form, name="categorias_form"),
    path('categorias_crear/', views.categorias_crear, name="categorias_crear"),
    path('categorias_actualizar/', views.categorias_actualizar, name="categorias_actualizar"),
    path('categorias_eliminar/<int:id>/', views.categorias_eliminar, name="categorias_eliminar"),
    path('categorias_formulario_editar/<int:id>/', views.categorias_formulario_editar, name="categorias_formulario_editar"),
]