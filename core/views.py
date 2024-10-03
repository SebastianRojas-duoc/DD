from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,update_session_auth_hash
import requests
# Create your views here.

def index(request):
    url = "https://wttr.in/Santiago,Chile?format=j1&lang=es"
    response = requests.get(url)
    clima_data = response.json()

    current_condition = clima_data['current_condition'][0]
    tomorrow_weather = clima_data['weather'][1]

    return render(request, 'core/index.html', {'clima': current_condition,'clima_manana': tomorrow_weather})
    


def comen(request):
    comentario=Comentario.objects.create(
        nombre=request.POST["nombre"],
        correo=request.POST["correo"],
        mensajes=request.POST["mensajes"],
    )
    comentario.save()
    mensaje="comentario enviado"
    context={"mensaje":mensaje}
    return render(request,'core/index.html',context)


def noti(request):
    noticias = Registronoti.objects.all()
    categorias = Categoria.objects.all()
    context = {'noticias': noticias, 'categorias': categorias}
    return render(request, 'core/noti.html', context)

@login_required
def add_noti(request):
    return render(request,'core/add_noti.html')

def regi(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            perfil = PerfilUsuario(
                user=user, 
                rut=form.cleaned_data['rut'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                genero=form.cleaned_data['genero']
            )
            perfil.save()
            return redirect('login')
        else:
            return render(request, 'registration/regi.html', {'form': form})
    else:
        form = RegistroForm()
        return render(request,'registration/regi.html', {'form': form})

def logins(request):
    error_message = None

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, " ")
    else:
        form = AuthenticationForm()
        
    return render(request, 'registration/login.html', {'form': form,'error_message':error_message})


def detalle_noti(request,noticia_id):
    noticia = get_object_or_404(Registronoti, id=noticia_id)
    
    context = {'noticia': noticia}
    return render(request, 'core/detalle_noti.html', context)

def detalle_noti1(request):
    return render(request,'core/detalle_noti1.html')

def detalle_noti2(request):
    return render(request,'core/detalle_noti2.html')

def detalle_noti3(request):
    return render(request,'core/detalle_noti3.html')

@login_required
def nuevo(request):
    if request.method == 'POST':
        categoria_id = request.POST["categoria"]
        categoria = Categoria.objects.get(id=categoria_id)
        
        noticia = Registronoti(
            categoria=categoria,
            titulo=request.POST["titulo"],
            subtitulo=request.POST["subtitulo"],
            reportero=request.POST["reportero"],
            link=request.POST["link"],
            fecha=request.POST["fecha"],
            descripcion=request.POST["descripcion"],
        )

        if 'imagen' in request.FILES:
            noticia.imagen = request.FILES['imagen']

        noticia.save()
        mensaje = "Noticia nuevo guardado"

        context = {
            'mensaje': mensaje,
            'categorias': Categoria.objects.all()
        }
		
        return render(request, 'core/add_noti.html', context)
    else:
        categorias = Categoria.objects.all()
        return render(request, 'core/add_noti.html', {'categorias': categorias})

@login_required
def add_noti(request):
	context = {"form" : NotiForm()}
	return render(request, 'core/add_noti.html', context)

@login_required
def usuario(request):
    perfil = PerfilUsuario.objects.get(user=request.user)
    return render(request, 'core/usuario.html', {'perfil': perfil})

@login_required
def mod_usuario(request):
    user = request.user
    perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ModificarUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()

            if form.cleaned_data.get('password'):
                update_session_auth_hash(request, user)

            return redirect('usuario')
    else:
        form = ModificarUsuarioForm(instance=user)


    return render(request, 'core/mod_usuario.html', {'form': form})

@login_required
def list_usuario(request):
    perfiles = PerfilUsuario.objects.all()
    return render(request,'core/list_usuario.html',{'perfiles':perfiles})

@login_required
def list_noti(request):
    noticias = Registronoti.objects.all()
    return render(request,'core/list_noti.html',{'noticias':noticias})

@login_required
def mod_noti(request, noti_id):
    noticia = get_object_or_404(Registronoti, pk=noti_id)

    if request.method == 'POST':
        form = NotiForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('list_noti')  
    else:
        form = NotiForm(instance=noticia)

    return render(request, 'core/mod_noti.html', {'form': form})

@login_required
def eliminar_usuario(request):
    user = request.user
    user.delete()
    return redirect(request,'core/index.html')

@login_required
def eliminar_noti(request,noticia_id):
    noticia = get_object_or_404(Registronoti, id=noticia_id)
    noticia.delete()
    return redirect(request,'core/list_noti.html')