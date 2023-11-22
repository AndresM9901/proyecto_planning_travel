<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def inicio(request):
    return render(request, 'planning_travel/inicio.html')

# Crud de Categorias
def categorias(request):
    # select * from categorias
    consulta = Categoria.objects.all()
    context = {'data': consulta}
    return render(request, 'planning_travel/categorias/categorias.html', context)

def categorias_form(request):
    return render(request, 'planning_travel/categorias/categorias_form.html')

def categorias_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Categoria(
                nombre=nombre,
                descripcion=descripcion
            )
            q.save()
            messages.success(request, "Fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('categorias_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('categorias_listar')

def categorias_eliminar(request, id):
    try:
        q = Categoria.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Categoria eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('categorias_listar')

def categorias_formulario_editar(request, id):

    q = Categoria.objects.get(pk = id)
    contexto = {'data': q}

    return render(request, 'planning_travel/categorias/categorias_form_editar.html', contexto)

def categorias_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Categoria.objects.get(pk = id)
            q.nombre = nombre
            q.descripcion = descripcion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('categorias_listar')


def index(request):
    return render(request, 'planning_travel/login/login.html')

# Crud de Usuarios

def usuarios(request):
    q = Usuario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/login/usuarios.html', contexto)

def usuarios_form(request):
    q = Rol.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/login/usuarios_form.html', contexto)

def usuarios_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rol = Usuario.objects.get(pk=request.POST.get("rol"))
        foto = request.FILES.get('foto')
        try:
            q = Usuario(
                nombre=nombre,
                correo=correo,
                contrasena=contrasena,
                rol=rol,
                foto=foto,
            )
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('usuarios_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('usuarios_listar')
    
def usuarios_eliminar(request, id):
    try:
        q = Usuario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Usuario eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('usuarios_listar')

def usuarios_form_editar(request, id):
    q = Usuario.objects.get(pk = id)
    contexto = {'data': q}

    return render(request, 'planning_travel/login/usuarios_form_editar.html', contexto)

def usuarios_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rol = Rol.objects.get(pk=request.POST.get('rol'))
        foto = request.POST.get('foto')
        try:
            q = Usuario.objects.get(pk = id)
            q.nombre = nombre
            q.correo = correo
            q.contrasena = contrasena
            q.rol = rol
            q.foto = foto
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('usuarios_listar')

# Crud de Hoteles

def hoteles(request):
    q = Hotel.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/hoteles/hoteles.html', contexto)

def hoteles_form(request):
    q = Categoria.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/hoteles/hoteles_form.html', contexto)

def hoteles_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        direccion = request.POST.get('direccion')
        categoria = Categoria.objects.get(pk=request.POST.get('categoria'))
        cantidad_habitacion = request.POST.get('cantidad_habitacion')
        try:
            q = Hotel(
                nombre=nombre,
                descripcion=descripcion,
                direccion=direccion,
                categoria=categoria,
                cantidad_habitacion=cantidad_habitacion,
            )
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('hoteles_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('usuarios_listar')
    
def hoteles_eliminar(request, id):
    try:
        q = Hotel.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Hotel eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('hoteles_listar')

def hoteles_form_editar(request, id):
    q = Hotel.objects.get(pk = id)
    c = Categoria.objects.all()
    contexto = {'data': q, 'categoria': c}

    return render(request, 'planning_travel/hoteles/hoteles_form_editar.html', contexto)

def hoteles_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        direccion = request.POST.get('direccion')
        categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
        cantidad_habitacion = request.POST.get('cantidad_habitacion')
        try:
            q = Hotel.objects.get(pk = id)
            q.nombre = nombre
            q.descripcion = descripcion
            q.direccion = direccion
            q.categoria = categoria
            q.cantidad_habitacion = cantidad_habitacion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

# Crud de puntuacion

def puntuaciones(request):
    q = Puntuacion.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/puntuaciones/puntuaciones.html', contexto)

def puntuaciones_form(request):
    q = Comentario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/puntuaciones/puntuaciones_form.html', contexto)

def puntuaciones_crear(request):
    if request.method == 'POST':
        comentario = Comentario.objects.get(pk=request.POST.get('comentario'))
        valoracion = request.POST.get('valoracion')
        try:
            q = Puntuacion(
                comentario=comentario,
                valoracion=valoracion,
            )
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('puntuaciones_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('puntuaciones_listar')
    
def puntuaciones_eliminar(request, id):
    try:
        q = Puntuacion.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Puntuacion eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')
        
def puntuaciones_form_editar(request, id):
    q = Puntuacion.objects.get(pk = id)
    c = Comentario.objects.all()
    contexto = {'data': q, 'comentario': c}
    return render(request, 'planning_travel/puntuaciones/puntuaciones_form_editar.html', contexto)

def puntuaciones_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        comentario = Comentario.objects.get(pk=request.POST.get('comentario'))
        valoracion = request.POST.get('valoracion')
        try:
            q = Usuario.objects.get(pk = id)
            q.comentario = comentario
            q.valoracion = valoracion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('puntuaciones_listar')

# Crud Comodidades

def comodidades(request):
    q = Comodidad.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/comodidades/comodidad.html', contexto)

def comodidades_form(request):
    return render(request, 'planning_travel/comodidades/comodidad_form.html')

def comodidades_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Comodidad(
                nombre=nombre,
                descripcion=descripcion
            )
            q.save()
            messages.success(request, "Fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('comodidades_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('comodidades_listar')
    
def comodidades_eliminar(request, id):
    try:
        q = Comodidad.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Comodidad eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('comodidades_listar')

def comodidades_form_editar(request, id):
    q = Comodidad.objects.get(pk = id)
    contexto = {'data': q}
    return render(request, 'planning_travel/comodidades/comodidad_form_editar.html', contexto)

def comodidades_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Comodidad.objects.get(pk = id)
            q.nombre = nombre
            q.descripcion = descripcion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('comodidades_listar')

# Crud habitaciones

def habitaciones(request):
    q = Habitacion.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/habitaciones/habitaciones.html', contexto)

def habitaciones_form(request):
    q = Hotel.objects.all()
    c = Foto.objects.all()
    contexto = {'data': q, 'foto': c}
    
    return render(request, 'planning_travel/habitaciones/habitaciones_form.html', contexto)

def habitaciones_crear(request):
    if request.method == 'POST':
        num_habitacion = request.POST.get('num_habitacion')
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        ocupado = request.POST.get('ocupado')
        ocupado = True if ocupado == 'on' else False    
        capacidad_huesped = request.POST.get('capacidad_huesped')
        tipoHabitacion = request.POST.get('tipoHabitacion')
        foto =  Foto.objects.get(pk=request.POST.get('foto'))
        precio = request.POST.get('precio')
        print(foto)
        try:
            q = Habitacion(
                num_habitacion = num_habitacion,
                id_hotel = hotel,
                ocupado = ocupado,
                capacidad_huesped = capacidad_huesped,
                tipoHabitacion = tipoHabitacion,
                foto = foto,
                precio = precio
            )
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('habitaciones_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('habitaciones_listar')

def habitaciones_eliminar(request, id):
    try:
        q = Habitacion.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Habitación eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')
    
    return redirect("habitaciones_listar")

def habitaciones_form_editar(request, id):
    c = Foto.objects.all()
    q = Hotel.objects.all()
    r = Habitacion.objects.get(pk = id)
    contexto = {'data': q, 'foto' : c, 'habitacion': r }
    return render(request, 'planning_travel/habitaciones/habitaciones_form_editar.html', contexto)

def habitaciones_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        num_habitacion = request.POST.get('num_habitacion')
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        ocupado = request.POST.get('ocupado')
        ocupado = True if ocupado == 'on' else False    
        capacidad_huesped = request.POST.get('capacidad_huesped')
        tipoHabitacion = request.POST.get('tipoHabitacion')
        foto =  Foto.objects.get(pk=request.POST.get('foto'))
        precio = request.POST.get('precio')
        try:
            q = Habitacion.objects.get(pk = id)
            q.num_habitacion = num_habitacion
            q.id_hotel = hotel
            q.ocupado = ocupado
            q.capacidad_huesped = capacidad_huesped
            q.tipoHabitacion = tipoHabitacion
            q.foto = foto
            q.precio = precio
          
            q.save()
            messages.success(request, "Fue actualizado correctamente")

        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('habitaciones_listar')

# Crud ReservaUsuarios

def reservas_usuarios(request):
    q = ReservaUsuario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/reservas_usuarios/reservas_usuarios.html', contexto)

def reservas_usuarios_form(request):
    q = Usuario.objects.all()
    c = Reserva.objects.all()
    contexto = {'data': q, 'reserva': c}
    
    return render(request, 'planning_travel/reservas_usuarios/reservas_usuarios_form.html', contexto)

def reservas_usuarios_crear(request):
    if request.method == 'POST':
        
        usuario = Usuario.objects.get(pk=request.POST.get('usuario'))
        reserva = Reserva.objects.get(pk=request.POST.get('reserva'))
        estado_reserva = request.POST.get('estado_reserva')
        fecha_realizacion = request.POST.get('fecha_realizacion')
        try:
            q = ReservaUsuario(
                usuario = usuario,
                reserva = reserva,
                estado_reserva = estado_reserva,
                fecha_realizacion = fecha_realizacion
            )
            q.save()
            messages.success(request, "Fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('reservas_usuarios_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('reservas_usuarios_listar')

def reservas_usuarios_eliminar(request, id):
    try:
        q = ReservaUsuario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Habitación eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')
    
    return redirect("reservas_usuarios_listar") 

def reservas_usuarios_form_editar(request, id):
    c = Usuario.objects.all()
    q = Reserva.objects.all()
    r = ReservaUsuario.objects.get(pk = id)
    contexto = {'data': r, 'usuario' : c, 'reserva': q }
    return render(request, 'planning_travel/reservas_usuarios/reservas_usuarios_form_editar.html', contexto)

def reservas_usuarios_actualizar(request):
    if request.method == 'POST': 
        id = request.POST.get('id')    
        usuario = Usuario.objects.get(pk=request.POST.get('usuario'))
        reserva = Reserva.objects.get(pk=request.POST.get('reserva'))
        estado_reserva = request.POST.get('estado_reserva')
        fecha_realizacion = request.POST.get('fecha_realizacion')
        try:
            q = ReservaUsuario.objects.get(pk = id)
            q.usuario = usuario
            q.reserva = reserva
            q.estado_reserva = estado_reserva
            q.fecha_realizacion = fecha_realizacion
          
            q.save()
            messages.success(request, "Fue actualizado correctamente")

        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('reservas_usuarios_listar')

#Crud HotelCategoria

def hoteles_categorias(request):
    q = HotelCategoria.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/hoteles_categorias/hoteles_categorias.html', contexto)

def hoteles_categorias_form(request):
    q = Hotel.objects.all()
    c = Categoria.objects.all()
    contexto = {'data': q, 'categoria': c}
    return render(request, 'planning_travel/hoteles_categorias/hoteles_categorias_form.html', contexto)

def hoteles_categorias_crear(request):
    if request.method == 'POST':
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        categoria = Categoria.objects.get(pk=request.POST.get('categoria'))
        try:
            q = HotelCategoria(
                id_hotel = hotel,
                id_categoria = categoria,
            )
            q.save()
            messages.success(request, "Fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('hoteles_categorias_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('hoteles_categorias_listar')
    
def hoteles_categorias_eliminar(request, id):
    try:
        q = HotelCategoria.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Hoteles categorias eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')
    
    return redirect("hoteles_categorias_listar") 

def hoteles_categorias_form_editar(request, id):
    c = Hotel.objects.all()
    q = Categoria.objects.all()
    r = HotelCategoria.objects.get(pk = id)
    contexto = {'data': r, 'hotel' : c, 'categoria': q }
    return render(request, 'planning_travel/hoteles_categorias/hoteles_categorias_form_editar.html', contexto)

def hoteles_categorias_actualizar(request):
    if request.method == 'POST': 
        id = request.POST.get('id')    
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        categoria = Categoria.objects.get(pk=request.POST.get('categoria'))
        try:
            q = HotelCategoria.objects.get(pk = id)
            q.id_hotel = hotel
            q.id_categoria = categoria
            q.save()
            messages.success(request, "Fue actualizado correctamente")

        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('hoteles_categorias_listar')
=======
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def inicio(request):
    return render(request, 'planning_travel/inicio.html')

# Crud de Categorias
def categorias(request):
    # select * from categorias
    consulta = Categoria.objects.all()
    context = {'data': consulta}
    return render(request, 'planning_travel/categorias/categorias.html', context)

def categorias_form(request):
    return render(request, 'planning_travel/categorias/categorias_form.html')

def categorias_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Categoria(
                nombre=nombre,
                descripcion=descripcion
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('categorias_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('categorias_listar')

def categorias_eliminar(request, id):
    try:
        q = Categoria.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Categoria eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('categorias_listar')

def categorias_formulario_editar(request, id):

    q = Categoria.objects.get(pk = id)
    contexto = {'data': q}

    return render(request, 'planning_travel/categorias/categorias_form_editar.html', contexto)

def categorias_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Categoria.objects.get(pk = id)
            q.nombre = nombre
            q.descripcion = descripcion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('categorias_listar')


def index(request):
    return render(request, 'planning_travel/login/login.html')

# Crud de Usuarios
def usuarios(request):
    q = Usuario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/login/usuarios.html', contexto)

def usuarios_form(request):
    return render(request, 'planning_travel/login/usuarios_form.html')

def usuarios_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rol = request.POST.get("rol")
        foto = request.FILES.get('foto')
        try:
            q = Usuario(
                nombre=nombre,
                correo=correo,
                contrasena=contrasena,
                rol=rol,
                foto=foto,
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('usuarios_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('usuarios_listar')
    
def usuarios_eliminar(request, id):
    try:
        q = Usuario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Usuario eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('usuarios_listar')

def usuarios_form_editar(request, id):
    q = Usuario.objects.get(pk = id)
    contexto = {'data': q}

    return render(request, 'planning_travel/login/usuarios_form_editar.html', contexto)

def usuarios_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rol = request.POST.get('rol')
        foto = request.POST.get('foto')
        try:
            q = Usuario.objects.get(pk = id)
            q.nombre = nombre
            q.correo = correo
            q.contrasena = contrasena
            q.rol = rol
            q.foto = foto
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('usuarios_listar')

# Crud de Hoteles
def hoteles(request):
    q = Hotel.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/hoteles/hoteles.html', contexto)

def hoteles_form(request):
    q = Categoria.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/hoteles/hoteles_form.html', contexto)

def hoteles_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        direccion = request.POST.get('direccion')
        categoria = Categoria.objects.get(pk=request.POST.get('categoria'))
        cantidad_habitaciones = request.POST.get('cantidad_habitaciones')
        try:
            q = Hotel(
                nombre=nombre,
                descripcion=descripcion,
                direccion=direccion,
                categoria=categoria,
                cantidad_habitaciones=cantidad_habitaciones,
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('hoteles_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('usuarios_listar')
    
def hoteles_eliminar(request, id):
    try:
        q = Hotel.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Hotel eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('hoteles_listar')

def hoteles_form_editar(request, id):
    q = Hotel.objects.get(pk = id)
    c = Categoria.objects.all()
    contexto = {'data': q, 'categoria': c}

    return render(request, 'planning_travel/hoteles/hoteles_form_editar.html', contexto)

def hoteles_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        direccion = request.POST.get('direccion')
        categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
        cantidad_habitaciones = request.POST.get('cantidad_habitaciones')
        try:
            q = Hotel.objects.get(pk = id)
            q.nombre = nombre
            q.descripcion = descripcion
            q.direccion = direccion
            q.categoria = categoria
            q.cantidad_habitaciones = cantidad_habitaciones
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('hoteles_listar')

# Crud de puntuacion
def puntuaciones(request):
    q = Puntuacion.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/puntuaciones/puntuaciones.html', contexto)

def puntuaciones_form(request):
    q = Comentario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/puntuaciones/puntuaciones_form.html', contexto)

def puntuaciones_crear(request):
    if request.method == 'POST':
        comentario = Comentario.objects.get(pk=request.POST.get('comentario'))
        valoracion = request.POST.get('valoracion')
        print(comentario)
        try:
            q = Puntuacion(
                id_comentario=comentario,
                valoracion=valoracion,
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('puntuaciones_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('puntuaciones_listar')
    
def puntuaciones_eliminar(request, id):
    try:
        q = Puntuacion.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Puntuacion eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('puntuaciones_listar')

def puntuaciones_form_editar(request, id):
    q = Puntuacion.objects.get(pk = id)
    c = Comentario.objects.all()
    contexto = {'data': q, 'comentario': c}
    return render(request, 'planning_travel/puntuaciones/puntuaciones_form_editar.html', contexto)

def puntuaciones_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        comentario = Comentario.objects.get(pk=request.POST.get('comentario'))
        valoracion = request.POST.get('valoracion')
        try:
            q = Puntuacion.objects.get(pk = id)
            q.id_comentario = comentario
            q.valoracion = valoracion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('puntuaciones_listar')

# Crud de fotos
def fotos(request):
    q = Foto.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/fotos/fotos.html', contexto)

def fotos_form(request):
    q = Hotel.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/fotos/fotos_form.html', contexto)

def fotos_crear(request):
    if request.method == 'POST':
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        url = request.FILES.get('url')
        descripcion = request.POST.get('descripcion')
        try:
            q = Foto(
                id_hotel=hotel,
                url_foto=url,
                descripcion=descripcion
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('fotos_listar')

def fotos_eliminar(request, id):
    try:
        q = Foto.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Foto eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('fotos_listar')

def fotos_form_editar(request, id):
    q = Foto.objects.get(pk = id)
    h = Hotel.objects.all()
    contexto = {'data': q, 'hotel': h}
    return render(request, 'planning_travel/fotos/fotos_form_editar.html', contexto)

def fotos_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        url = request.FILES.get('url')
        descripcion = request.POST.get('descripcion')
        try:
            q = Foto.objects.get(pk = id)
            q.id_hotel = hotel
            q.url_foto = url
            q.descripcion = descripcion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('hoteles_listar')

# Crud de HotelComodidad
def hoteles_comodidades(request):
    q = HotelComodidad.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/hoteles_comodidades/hoteles_comodidades.html', contexto)

def hoteles_comodidades_form(request):
    q = Hotel.objects.all()
    c = Comodidad.objects.all()
    contexto = {'hotel': q, 'comodidad': c}
    return render(request, 'planning_travel/hoteles_comodidades/hoteles_comodidades_form.html', contexto)

def hoteles_comodidades_crear(request):
    if request.method == 'POST':
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        comodidad = Comodidad.objects.get(pk=request.POST.get('comodidad'))
        dispone = request.POST.get('dispone')
        dispone = True if dispone == 'on' else False
        try:
            q = HotelComodidad(
                id_hotel=hotel,
                id_comodidad=comodidad,
                dispone=dispone
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('hoteles_comodidades_listar')

def hoteles_comodidades_eliminar(request, id):
    try:
        q = HotelComodidad.objects.get(pk = id)
        q.delete()
        messages.success(request, 'HotelComodidad eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('hoteles_comodidades_listar')

def hoteles_comodidades_form_editar(request, id):
    q = HotelComodidad.objects.get(pk = id)
    h = Hotel.objects.all()
    c = Comodidad.objects.all()
    contexto = {'data': q, 'hotel': h, 'comodidad': c}
    return render(request, 'planning_travel/hoteles_comodidades/hoteles_comodidades_form_editar.html', contexto)

def hoteles_comodidades_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        hotel = Hotel.objects.get(pk=request.POST.get('hotel'))
        comodidad = Comodidad.objects.get(pk=request.POST.get('comodidad'))
        dispone = request.POST.get('dispone')
        dispone = True if dispone == 'on' else False
        try:
            q = HotelComodidad.objects.get(pk = id)
            q.id_hotel = hotel
            q.id_comodidad = comodidad
            q.dispone = dispone
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('hoteles_comodidades_listar')

# Crud de Reservas
def reservas(request):
    q = Reserva.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/reservas/reservas.html', contexto)

def reservas_form(request):
    q = Habitacion.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/reservas/reservas_form.html', contexto)

def reservas_crear(request):
    if request.method == 'POST':
        habitacion = Habitacion.objects.get(pk=request.POST.get('habitacion'))
        fecha_llegada = request.POST.get('fecha_llegada')
        fecha_salida = request.POST.get('fecha_salida')
        cantidad_personas = request.POST.get('cantidad_personas')
        print(fecha_llegada)
        try:
            q = Reserva(
                habitacion=habitacion,
                fecha_llegada=fecha_llegada,
                fecha_salida=fecha_salida,
                cantidadPersonas=cantidad_personas
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('reservas_listar')

def reservas_eliminar(request, id):
    try:
        q = Reserva.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Reserva eliminada correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('reservas_listar')

def reservas_form_editar(request, id):
    q = Reserva.objects.get(pk = id)
    h = Habitacion.objects.all()
    contexto = {'data': q, 'habitacion': h}
    return render(request, 'planning_travel/reservas/reservas_form_editar.html', contexto)

def reservas_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        habitacion = Habitacion.objects.get(pk=request.POST.get('habitacion'))
        fecha_llegada = request.POST.get('fecha_llegada')
        fecha_salida = request.POST.get('fecha_salida')
        cantidad_personas = request.POST.get('cantidad_personas')
        try:
            q = Reserva.objects.get(pk = id)
            q.id_habitacion = habitacion
            q.fecha_llegada = fecha_llegada
            q.fecha_salida = fecha_salida
            q.cantidadPersonas = cantidad_personas
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('reservas_listar')
>>>>>>> ec4f9b8d04c85013495e14467148acb359621971
