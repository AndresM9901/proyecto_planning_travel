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
    # Crud de Reportes
    path('reportes_listar/', views.reportes, name="reportes_listar"),
    path('reportes_form/', views.reportes_form, name="reportes_form"),
    path('reportes_crear/', views.reportes_crear, name="reportes_crear"),
    path('reportes_actualizar/', views.reportes_actualizar, name="reportes_actualizar"),
    path('reportes_eliminar/<int:id>', views.reportes_eliminar, name="reportes_eliminar"),
    path('reportes_formulario_editar/<int:id>/', views.reportes_formulario_editar, name="reportes_formulario_editar"),
    # Crud de Reportes Moderador
    path('reportesModerador_listar/', views.reportesModerador, name="reportesModerador_listar"),
    path('reportesModerador_form/', views.reportesModerador_form, name="reportesModerador_form"),
    path('reportesModerador_crear/', views.reportesModerador_crear, name="reportesModerador_crear"),
    path('reportesModerador_actualizar/', views.reportesModerador_actualizar, name="reportesModerador_actualizar"),
    path('reportesModerador_eliminar/<int:id>', views.reportesModerador_eliminar, name="reportesModerador_eliminar"),
    path('reportesModerador_form_editar/<int:id>/', views.reportesModerador_form_editar, name="reportesModerador_form_editar"),
    # Crud de Clientes
    path('clientes_listar/', views.clientes, name="clientes_listar"),
    path('clientes_form/', views.clientes_form, name="clientes_form"),
    path('clientes_crear/', views.clientes_crear, name="clientes_crear"),
    path('clientes_actualizar/', views.clientes_actualizar, name="clientes_actualizar"),
    path('clientes_eliminar/<int:id>', views.clientes_eliminar, name="clientes_eliminar"),
    path('clientes_form_editar/<int:id>/', views.clientes_form_editar, name="clientes_form_editar"),
    # Crud de Perfil Usuarios
    path('perfilUsuarios_listar/', views.perfilUsuarios, name="perfilUsuarios_listar"),
    path('perfilUsuarios_form/', views.perfilUsuarios_form, name="perfilUsuarios_form"),
    path('perfilUsuarios_crear/', views.perfilUsuarios_crear, name="perfilUsuarios_crear"),
    path('perfilUsuarios_actualizar/', views.perfilUsuarios_actualizar, name="perfilUsuarios_actualizar"),
    path('perfilUsuarios_eliminar/<int:id>', views.perfilUsuarios_eliminar, name="perfilUsuarios_eliminar"),
    path('perfilUsuarios_form_editar/<int:id>/', views.perfilUsuarios_form_editar, name="perfilUsuarios_form_editar"),



]