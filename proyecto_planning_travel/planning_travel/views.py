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

def comentarios(request):
    q = Comentario.objects.all()
    e = Hotel.objects.all()
    c = Usuario.objects.all()
    contexto = {'data': q, 'usuario': c}
    return render(request, 'planning_travel/comentarios/comentarios.html', contexto)

def comentarios_form(request):
    q = Hotel.objects.all()
    c = Usuario.objects.all()
    contexto = {'data': q, 'usuario': c}
    return render(request, 'planning_travel/comentarios/comentarios_form.html',contexto)

def comentarios_crear(request):
    if request.method == 'POST':
        id_hotel = Hotel.objects.get(pk=request.POST.get('id_hotel'))
        id_usuario = Usuario.objects.get(pk=request.POST.get('id_usuario'))
        contenido = request.POST.get('contenido')
        fecha = request.POST.get('fecha')

        try:
            q = Comentario(
                id_hotel=id_hotel,
                id_usuario=id_usuario,
                contenido=contenido,
                fecha=fecha
            )
            q.save()
            messages.success(request, "Fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('comentarios_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('comentarios_listar')
    
def comentarios_eliminar(request, id):
    try:
        q = Comentario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Comentario eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('comentarios_listar')

def comentarios_form_editar(request, id):
    q = Comentario.objects.get(pk = id)
    c = Hotel.objects.all()
    e = Usuario.objects.all()
    contexto = {'data': q, 'hotel': c, 'usuario': e}
    return render(request, 'planning_travel/comentarios/comentarios_form_editar.html', contexto)


def comentarios_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        id_hotel = Hotel.objects.get(pk=request.POST.get("id_hotel"))
        id_usuario = Usuario.objects.get(pk=request.POST.get("id_usuario"))
        contenido = request.POST.get('contenido')
        fecha = request.POST.get('fecha')
        print(fecha)

        try:
            q = Comentario.objects.get(pk = id)
            q.id_hotel = id_hotel
            q.id_usuario = id_usuario
            q.contenido = contenido
            q.fecha = fecha
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('comentarios_listar')


def roles(request):
    consulta = Rol.objects.all()
    context = {'data': consulta}
    return render(request, 'planning_travel/roles/roles.html', context)

def roles_form(request):
    return render(request, 'planning_travel/roles/roles_form.html')
def roles_crear(request):
    if request.method == 'POST':
        nombre= request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        permisos = request.POST.get('permisos')

        try:
            q = Rol(
                nombre=nombre,
                descripcion=descripcion,
                permisos=permisos,
            )
            q.save()
            messages.success(request, "Fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('roles_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('roles_listar')
    
def roles_eliminar(request, id):
    try:
        q = Rol.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Rol eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('roles_listar')

def roles_formulario_editar(request, id):

    q = Rol.objects.get(pk = id)
    contexto = {'data': q}

    return render(request, 'planning_travel/roles/roles_form_editar.html', contexto)
def roles_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre= request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        permisos = request.POST.get('permisos')

        try:
            q = Rol.objects.get(pk = id)
            q.nombre= nombre
            q.descripcion = descripcion
            q.permisos = permisos
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

    else:
            messages.warning(request,'No se enviaron datos')
    return redirect('roles_listar')


def favoritos(request):
    consulta = Favorito.objects.all()
    context = {'data': consulta}
    return render(request, 'planning_travel/favoritos/favoritos.html', context)

def favoritos_form(request):
    q = Hotel.objects.all()
    c = Usuario.objects.all()
    contexto = {'data': q, 'usuario': c}
    return render(request, 'planning_travel/favoritos/favoritos_form.html', contexto)

def favoritos_crear(request):
    if request.method == 'POST':
        id_hotel = Hotel.objects.get(pk=request.POST.get('id_hotel'))
        id_usuario = Usuario.objects.get(pk=request.POST.get('id_usuario'))
        fecha_agregado = request.POST.get('fecha_agregado')

        try:
            q = Favorito(
                id_hotel=id_hotel,
                id_usuario=id_usuario,
                fecha_agregado=fecha_agregado,
            )
            q.save()
            messages.success(request, "Fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('favoritos_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('favoritos_listar')

def favoritos_eliminar(request, id):
    try:
        q = Favorito.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Hotel favorito eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('favoritos_listar')


def favoritos_formulario_editar(request, id):
    q = Favorito.objects.get(pk = id)
    c = Hotel.objects.all()
    e = Usuario.objects.all()
    contexto = {'data': q, 'hotel': c, 'usuario': e}
    return render(request, 'planning_travel/favoritos/favoritos_form_editar.html', contexto)


def favoritos_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        id_hotel = Hotel.objects.get(pk=request.POST.get("id_hotel"))
        id_usuario = Usuario.objects.get(pk=request.POST.get("id_usuario"))
        fecha_agregado = request.POST.get('fecha_agregado')

        try:
            q = Favorito.objects.get(pk = id)
            q.id_hotel= id_hotel
            q.id_usuario = id_usuario
            q.fecha_agregado=fecha_agregado
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
        
    return redirect('favoritos_listar')



