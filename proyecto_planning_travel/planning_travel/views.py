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
            messages.success(request, "Fue actualizado correctamente")
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
