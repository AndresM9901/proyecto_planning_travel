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
    context = {'data': q, 'usuario': u, 'reporte': r}
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
