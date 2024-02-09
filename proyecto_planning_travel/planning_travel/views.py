from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .serializers import *
from rest_framework import viewsets

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

# Crud reportes
def reportes(request):
    consulta = Reportes.objects.all()
    context = {'data': consulta}
    return render(request, 'planning_travel/reportes/reportes.html', context)

def reportes_form(request):
    q = Usuario.objects.all()
    context = {'usuario': q}
    return render(request, 'planning_travel/reportes/reportes_form.html', context)

def reportes_crear(request):
    if request.method == 'POST':
        id_usuario =Usuario.objects.get(pk = request.POST.get('id_usuario'))
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Reportes(
                id_usuario=id_usuario,
                nombre= nombre,
                descripcion= descripcion
            )
            q.save()
            messages.success(request, "El reporte fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('reportes_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('reportes_listar')

def reportes_actualizar(request):
    if request.method == 'POST':
        id= request.POST.get('id')
        id_usuario =Usuario.objects.get(pk = request.POST.get('id_usuario'))
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Reportes.objects.get(pk = id)
            q.id_usuario=id_usuario
            q.nombre = nombre
            q.descripcion = descripcion
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('reportes_listar')

def reportes_eliminar(request, id):
    try:
        q = Reportes.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Reporte eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('reportes_listar')

def reportes_form_editar(request, id):
    q = Usuario.objects.all()
    r = Reportes.objects.get(pk = id)
    context = { 'usuario' : q , 'data' : r }
    return render(request, 'planning_travel/reportes/reportes_form_editar.html', context)

# Crud reportes moderador
def reportesModerador(request):
    q = ReporteModerador.objects.all()
    context = {'data': q}
    return render(request, 'planning_travel/reportesModerador/reportesModerador.html', context)

def reportesModerador_form(request):
    q = Usuario.objects.all()
    r = Reportes.objects.all()
    context = { 'usuario' : q , 'reporte' : r }
    return render(request, 'planning_travel/reportesModerador/reportesModerador_form.html', context)

def reportesModerador_crear(request):
    if request.method == 'POST':
        id_usuario = Usuario.objects.get(pk = request.POST.get('id_usuario'))
        id_reporte = Reportes.objects.get(pk = request.POST.get('id_reporte'))
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        try:
            q = ReporteModerador(
                id_usuario=id_usuario,
                id_reporte=id_reporte,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('reportesModerador_listar')

def reportesModerador_eliminar(request, id):
    try:
        q = ReporteModerador.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Reporte eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('reportesModerador_listar')

def reportesModerador_form_editar(request, id):
    q = ReporteModerador.objects.get(pk = id)
    u = Usuario.objects.all()
    r = Reportes.objects.all()
    context = {'data': q, 'usuario': u, 'reporte':r}
    return render(request, 'planning_travel/reportesModerador/reportesModerador_form_editar.html', context)

def reportesModerador_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        id_reporte = Reportes.objects.get(pk = request.POST.get('id_reporte'))
        id_usuario = Usuario.objects.get(pk = request.POST.get('id_usuario'))
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        try:
            q = ReporteModerador.objects.get(pk = id)
            q.fecha_inicio = fecha_inicio
            q.fecha_fin = fecha_fin
            q.id_reporte = id_reporte
            q.id_usuario = id_usuario
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('reportesModerador_listar')

# Crud cliente
def clientes(request):
    q = Cliente.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/clientes/clientes.html', contexto)

def clientes_form(request):
    q = Usuario.objects.all()
    context= {'data': q}
    return render(request, 'planning_travel/clientes/clientes_form.html', context)

def clientes_crear(request):
    if request.method == 'POST':
        id_usuario = Usuario.objects.get(pk = request.POST.get('id_usuario'))
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        fotoPerfil = request.POST.get('fotoPerfil')
        try:
            q = Cliente(
                id_usuario=id_usuario,
                nombre=nombre,
                numero_contacto=numero_contacto,
                fotoPerfil=fotoPerfil
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'error')
    return redirect('clientes_listar')

def clientes_eliminar(request, id):
    try:
        q = Cliente.objects.get(pk = id)
        q.delete()
        messages.success(request, 'cliente eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('clientes_listar')

def clientes_form_editar(request, id):
    q = Cliente.objects.get(pk = id)
    c = Usuario.objects.all()
    context = { 'data': q , 'usuario': c }
    return render(request, 'planning_travel/clientes/clientes_form_editar.html', context)

def clientes_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        id_usuario  = Usuario.objects.get(pk = request.POST.get('id_usuario'))
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        fotoPerfil = request.POST.get('fotoPerfil')
        try:
            q = Cliente.objects.get(pk = id)
            q.nombre = nombre
            q.id_usuario = id_usuario
            q.numero_contacto = numero_contacto            
            q.fotoPerfil = fotoPerfil
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('clientes_listar')

# Crud perfil Usuario
def perfilUsuarios(request):
    q = PerfilUsuario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/perfilUsuarios/perfilUsuarios.html', contexto)

def perfilUsuarios_form(request):
    q = Usuario.objects.all()
    h = Hotel.objects.all()
    context = { 'usuarios' : q , 'hotel' : h }
    return render(request, 'planning_travel/perfilUsuarios/perfilUsuarios_form.html', context)

def perfilUsuarios_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        id_usuario = Usuario.objects.get(pk = request.POST.get('id_usuario'))
        id_hotel = Hotel.objects.get(pk = request.POST.get('id_hotel'))
        fotoPerfil = request.POST.get('fotoPerfil')
        try:
            q = PerfilUsuario(
                nombre=nombre,
                numero_contacto=numero_contacto,
                id_hotel=id_hotel,
                id_usuario=id_usuario,
                fotoPerfil=fotoPerfil
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'error')
    return redirect('perfilUsuarios_listar')

def perfilUsuarios_eliminar(request, id):
    try:
        q = PerfilUsuario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('perfilUsuarios_listar')

def perfilUsuarios_form_editar(request, id):
    q = PerfilUsuario.objects.get(pk = id)
    u = Usuario.objects.all()
    h = Hotel.objects.all()
    context = {'data': q , 'hotel': h, 'usuarios' : u}
    return render(request, 'planning_travel/perfilUsuarios/perfilUsuarios_form_editar.html', context)

def perfilUsuarios_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        id_usuario = Usuario.objects.get(pk = request.POST.get('id_usuario'))
        id_hotel = Hotel.objects.get(pk = request.POST.get('id_hotel'))
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        fotoPerfil = request.POST.get('fotoPerfil')
        try:
            q = PerfilUsuario.objects.get(pk = id)
            q.id_usuario = id_usuario
            q.id_hotel = id_hotel
            q.nombre = nombre
            q.numero_contacto = numero_contacto            
            q.fotoPerfil = fotoPerfil
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('perfilUsuarios_listar')

# api base de datos
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ComodidadViewSet(viewsets.ModelViewSet):
    queryset = Comodidad.objects.all()
    serializer_class = ComodidadSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSeralizer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class PuntuacionViewSet(viewsets.ModelViewSet):
    queryset = Puntuacion.objects.all()
    serializer_class = PuntuacionSerializer

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

class HotelComodidadViewSet(viewsets.ModelViewSet):
    queryset = HotelComodidad.objects.all()
    serializer_class = HotelComodidadSerializer

class HotelCategoriaViewSet(viewsets.ModelViewSet):
    queryset = HotelCategoria.objects.all()
    serializer_class = HotelCategoriaSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ReservaUsuario.objects.all()
    serializer_class = ReservaUsuarioSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ReporteModeradorViewSet(viewsets.ModelViewSet):
    queryset = ReporteModerador.objects.all()
    serializer_class = ReporteModeradorSerializer