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

     path('comentarios_listar/', views.comentarios, name="comentarios_listar"),
    path('comentarios_form/', views.comentarios_form, name="comentarios_form"),
    path('comentarios_crear/', views.comentarios_crear, name="comentarios_crear"),
    path('comentarios_actualizar/', views.comentarios_actualizar, name="comentarios_actualizar"),
    path('comentarios_eliminar/<int:id>/', views.comentarios_eliminar, name="comentarios_eliminar"),
    path('comentarios_form_editar/<int:id>/', views.comentarios_form_editar, name="comentarios_form_editar"),
    
    
    path('roles_listar/', views.roles, name="roles_listar"),
    path('roles_form/', views.roles_form, name="roles_form"),
    path('roles_crear/', views.roles_crear, name="roles_crear"),
    path('roles_actualizar/', views.roles_actualizar, name="roles_actualizar"),
    path('roles_eliminar/<int:id>/', views.roles_eliminar, name="roles_eliminar"),
    path('roles_formulario_editar/<int:id>/', views.roles_formulario_editar, name="roles_formulario_editar"),

    path('favoritos_listar/', views.favoritos, name="favoritos_listar"),
    path('favoritos_form/', views.favoritos_form, name="favoritos_form"),
    path('favoritos_crear/', views.favoritos_crear, name="favoritos_crear"),
    path('favoritos_actualizar/', views.favoritos_actualizar, name="favoritos_actualizar"),
    path('favoritos_eliminar/<int:id>/', views.favoritos_eliminar, name="favoritos_eliminar"),
    path('favoritos_formulario_editar/<int:id>/', views.favoritos_formulario_editar, name="favoritos_formulario_editar"),

    
    
]