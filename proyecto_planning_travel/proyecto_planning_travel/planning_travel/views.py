from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def inicio(request):
    return render(request, 'planning_travel/inicio.html')

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

    return render(request, 'planning_travel/categorias/categorias_formulario_editar.html', contexto)

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

def usuarios(request):
    q = Usuario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/login/usuarios.html', contexto)

def usuarios_form(request):
    q = Usuario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/login/usuarios_form.html', contexto)

# reportes
def reportes(request):
    consulta = Reporte.objects.all()
    context = {'data': consulta}
    return render(request, 'planning_travel/reportes/reportes.html', context)

def reportes_form(request):
    return render(request, 'planning_travel/reportes/reportes_form.html')

def reportes_crear(request):
    if request.method == 'POST':
        id_usuario =request.POST.get('id_usuario')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Reporte(
                id_usuario=id_usuario,
                nombre= nombre,
                descripcion= descripcion
            )
            q.save(nombre,descripcion)
            messages.success(request, "El reporte fue agregado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('reportes_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('reportes_listar')

def reportes_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Reporte.objects.get(pk = id)
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
        q = Reporte.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Reporte eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('reportes_listar')

def reportes_formulario_editar(request, id):

    q = Reporte.objects.get(pk = id)
    contexto = {'data': q}

    return render(request, 'planning_travel/reportes/reportes_formulario_editar.html', contexto)

# reportes moderador
def reportesModerador(request):
    q = ReporteModerador.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/reportesModerador/reportesModerador.html', contexto)

def reportesModerador_form(request):
    return render(request, 'planning_travel/reportesModerador/reportesModerador_form.html')

def reportesModerador_crear(request):
    if request.method == 'POST':
        id_usuario =request.POST.get('id_usuario')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        print(fecha_inicio)
        try:
            q = ReporteModerador(
                id_usuario=id_usuario,
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
    contexto = {'data': q}
    return render(request, 'planning_travel/reportesModerador/reportesModerador_form_editar.html', contexto)

def reportesModerador_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        try:
            q = ReporteModerador.objects.get(pk = id)
            q.fecha_inicio = fecha_inicio
            q.fecha_fin = fecha_fin
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('reportesModerador_listar')

# cliente
def clientes(request):
    q = Cliente.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/clientes/clientes.html', contexto)

def clientes_form(request):
    q= Usuario.objects.all()
    context= {'data':q}
    return render(request, 'planning_travel/clientes/clientes_form.html', context)

def clientes_crear(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        fotoPerfil = request.POST.get('fotoPerfil')
        print(nombre)
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

    return redirect('cliente_listar')

def clientes_form_editar(request, id):
    q = Cliente.objects.get(pk = id)
    contexto = {'data': q}
    return render(request, 'planning_travel/clientes/clientes_form_editar.html', contexto)

def clientes_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        fotoPerfil = request.POST.get('fotoPerfil')
        try:
            q = Cliente.objects.get(pk = id)
            q.nombre = nombre
            q.numero_contacto = numero_contacto            
            q.fotoPerfil = fotoPerfil
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')
    return redirect('clientes_listar')

# perfil Usuario
def perfilUsuarios(request):
    q = PerfilUsuario.objects.all()
    contexto = {'data': q}
    return render(request, 'planning_travel/perfilUsuarios/perfilUsuarios.html', contexto)

def perfilUsuarios_form(request):
    return render(request, 'planning_travel/perfilUsuarios/perfilUsuarios_form.html')

def perfilUsuarios_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        fotoPerfil = request.POST.get('fotoPerfil')
        print(nombre)
        try:
            q = PerfilUsuario(
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
    contexto = {'data': q}
    return render(request, 'planning_travel/perfilUsuarios/perfilUsuarios_form_editar.html', contexto)

def perfilUsuarios_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        numero_contacto = request.POST.get('numero_contacto')
        fotoPerfil = request.POST.get('fotoPerfil')
        try:
            q = PerfilUsuario.objects.get(pk = id)
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
