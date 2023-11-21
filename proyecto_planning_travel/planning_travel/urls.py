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
    # Crud de Fotos
    path('fotos_listar/', views.fotos, name='fotos_listar'),
    path('fotos_form/', views.fotos_form, name='fotos_form'),
    path('fotos_crear/', views.fotos_crear, name='fotos_crear'),
    path('fotos_actualizar/', views.fotos_actualizar, name='fotos_actualizar'),
    path('fotos_eliminar/<int:id>', views.fotos_eliminar, name='fotos_eliminar'),
    path('fotos_form_editar/<int:id>', views.fotos_form_editar, name='fotos_form_editar'),
    # Crud de hotelComodidad
    path('hoteles_comodidades_listar/', views.hoteles_comodidades, name='hoteles_comodidades_listar'),
    path('hoteles_comodidades_form/', views.hoteles_comodidades_form, name='hoteles_comodidades_form'),
    path('hoteles_comodidades_crear/', views.hoteles_comodidades_crear, name='hoteles_comodidades_crear'),
    path('hoteles_comodidades_actualizar/', views.hoteles_comodidades_actualizar, name='hoteles_comodidades_actualizar'),
    path('hoteles_comodidades_eliminar/<int:id>', views.hoteles_comodidades_eliminar, name='hoteles_comodidades_eliminar'),
    path('hoteles_comodidades_form_editar/<int:id>', views.hoteles_comodidades_form_editar, name='hoteles_comodidades_form_editar'),
    # Crud de Reservas
    path('reservas_listar/', views.reservas, name='reservas_listar'),
    path('reservas_form/', views.reservas_form, name='reservas_form'),
    path('reservas_crear/', views.reservas_crear, name='reservas_crear'),
    path('reservas_actualizar/', views.reservas_actualizar, name='reservas_actualizar'),
    path('reservas_eliminar/<int:id>', views.reservas_eliminar, name='reservas_eliminar'),
    path('reservas_form_editar/<int:id>', views.reservas_form_editar, name='reservas_form_editar'),
]