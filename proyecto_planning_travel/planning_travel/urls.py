from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    # path('', views.index, name="index"),
    # Crud de Categorias
    path('categorias_listar/', views.categorias, name="categorias_listar"),
    path('categorias_form/', views.categorias_form, name="categorias_form"),
    path('categorias_crear/', views.categorias_crear, name="categorias_crear"),
    path('categorias_actualizar/', views.categorias_actualizar, name="categorias_actualizar"),
    path('categorias_eliminar/<int:id>/', views.categorias_eliminar, name="categorias_eliminar"),
    path('categorias_formulario_editar/<int:id>/', views.categorias_formulario_editar, name="categorias_formulario_editar"),
    # Crud de Usuarios
    path('usuarios_listar/', views.usuarios, name='usuarios_listar'),
    path('usuarios_form/', views.usuarios_form, name='usuarios_form'),
    path('usuarios_crear/', views.usuarios_crear, name='usuarios_crear'),
    path('usuarios_actualizar/', views.usuarios_actualizar, name='usuarios_actualizar'),
    path('usuarios_eliminar/<int:id>/', views.usuarios_eliminar, name='usuarios_eliminar'),
    path('usuarios_form_editar/<int:id>/', views.usuarios_form_editar, name='usuarios_form_editar'),
    # Crud de hotel
    path('hoteles_listar/', views.hoteles, name='hoteles_listar'),
    path('hoteles_form/', views.hoteles_form, name='hoteles_form'),
    path('hoteles_crear/', views.hoteles_crear, name='hoteles_crear'),
    path('hoteles_actualizar/', views.hoteles_actualizar, name='hoteles_actualizar'),
    path('hoteles_eliminar/<int:id>', views.hoteles_eliminar, name='hoteles_eliminar'),
    path('hoteles_form_editar/<int:id>', views.hoteles_form_editar, name='hoteles_form_editar'),
    # Crud de puntuaciones
    path('puntuaciones_listar/', views.puntuaciones, name='puntuaciones_listar'),
    path('puntuaciones_form/', views.puntuaciones_form, name='puntuaciones_form'),
    path('puntuaciones_crear/', views.puntuaciones_crear, name='puntuaciones_crear'),
    path('puntuaciones_actualizar/', views.puntuaciones_actualizar, name='puntuaciones_actualizar'),
    path('puntuaciones_eliminar/<int:id>', views.puntuaciones_eliminar, name='puntuaciones_eliminar'),
    path('puntuaciones_form_editar/<int:id>', views.puntuaciones_form_editar, name='puntuaciones_form_editar'),


    # Crud de Comodidades
    path('comodidades_listar/', views.comodidades, name='comodidades_listar'),
    path('comodidades_form/', views.comodidades_form, name='comodidades_form'),
    path('comodidades_crear/', views.comodidades_crear, name='comodidades_crear'),
    path('comodidades_eliminar/<int:id>', views.comodidades_eliminar, name='comodidades_eliminar'),
    path('comodidades_form_editar/<int:id>', views.comodidades_form_editar, name='comodidades_formulario_editar'),
    path('comodidades_actualizar/', views.comodidades_actualizar, name='comodidades_actualizar'),

]