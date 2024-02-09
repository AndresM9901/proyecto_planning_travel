from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'rol', views.RolViewSet)
router.register(r'producto', views.ProductoViewSet)
router.register(r'hotel', views.HotelViewSet)
router.register(r'comodidad', views.ComodidadViewSet)
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'favorito', views.FavoritoViewSet)
router.register(r'comentario', views.ComentarioViewSet)
router.register(r'puntucion', views.PuntuacionViewSet)
router.register(r'foto', views.FotoViewSet)
router.register(r'hotel-comodidad', views.HotelComodidadViewSet)
router.register(r'hotel-categoria', views.HotelCategoriaViewSet)
router.register(r'habitacion', views.HabitacionViewSet)
router.register(r'reserva', views.ReservaViewSet)
router.register(r'reserva-usuario', views.ReservaUsuarioViewSet)
router.register(r'perfil-usuario', views.PerfilUsuarioViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'reporte', views.ReporteViewSet)
router.register(r'reporte-moderador', views.ReporteModeradorViewSet)

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('api/1.0/', include(router.urls)),
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

    # Crud de habitaciones

    path('habitaciones_listar/', views.habitaciones, name="habitaciones_listar"),
    path('habitaciones_form/', views.habitaciones_form, name="habitaciones_form"),
    path('habitaciones_crear/', views.habitaciones_crear, name="habitaciones_crear"),
    path('habitaciones_eliminar/<int:id>', views.habitaciones_eliminar, name="habitaciones_eliminar"),
    path('habitaciones_form_editar/<int:id>', views.habitaciones_form_editar, name='habitaciones_form_editar'),
    path('habitaciones_actualizar/', views.habitaciones_actualizar, name='habitaciones_actualizar'),

    #Crud de ReservaUsuario

    path('reservas_usuarios_listar/', views.reservas_usuarios, name="reservas_usuarios_listar"),
    path('reservas_usuarios_form/', views.reservas_usuarios_form, name="reservas_usuarios_form"),
    path('reservas_usuarios_crear/', views.reservas_usuarios_crear, name="reservas_usuarios_crear"),
    path('reservas_usuarios_eliminar/<int:id>', views.reservas_usuarios_eliminar, name="reservas_usuarios_eliminar"),
    path('reservas_usuarios_form_editar/<int:id>', views.reservas_usuarios_form_editar, name='reservas_usuarios_form_editar'),
    path('reservas_usuarios_actualizar/', views.reservas_usuarios_actualizar, name='reservas_usuarios_actualizar'),

    # Crud de HotelCategoria

    path('hoteles_categorias_listar/', views.hoteles_categorias, name="hoteles_categorias_listar"),
    path('hoteles_categorias_form/', views.hoteles_categorias_form, name="hoteles_categorias_form"),
    path('hoteles_categorias_crear/', views.hoteles_categorias_crear, name="hoteles_categorias_crear"),
    path('hoteles_categorias_eliminar/<int:id>', views.hoteles_categorias_eliminar, name="hoteles_categorias_eliminar"),
    path('hoteles_categorias_form_editar/<int:id>', views.hoteles_categorias_form_editar, name='hoteles_categorias_form_editar'),
    path('hoteles_categorias_actualizar/', views.hoteles_categorias_actualizar, name='hoteles_categorias_actualizar'),
]