from msilib.schema import RadioButton
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import Decano, Facultad, Estudiante, EstadoVotacion, TipoVotacion, Votacion,Candidato, Voto
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    return HttpResponse('vamos a comerrers')


# def categorias(request):
#     contexto = {
#         'titulo': 'Blockbuster',
#         'holabb': 'hola guapoooo',
#         'categorias': [
#             {'id': 1, 'nombre': 'die hard'},
#             {'id': 2, 'nombre': 'lethal weapon'},
#         ],
#     }
#     return render(request, 'app/categorias.html',contexto) #para dibujar la pagina


# def categoria(request, id):
#     numeros = [1, 2, 3]
#     print(id)
#     print(numeros)
#     return HttpResponse(f'Esta es la categoria {id}')

def menu_decano(request):
    return render(request, 'app/menu_decano.html')

def cambiar_estado(request):
    return render(request, 'app/cambiar_estado.html')

def candidatos_ganadores(request):
    return render(request, 'app/candidatos-ganadores.html')

def candidatos_ganadores2(request):
    return render(request, 'app/candidatos-ganadores2.html')

def consult_candidatos_es(request):
    return render(request, 'app/consult-candidatos-es.html')

def consult_candidatos(request):
    return render(request, 'app/consult-candidatos.html')

def consult_estudiante(request):
    return render(request, 'app/consult-estudiante.html')

def consult(request):
    return render(request, 'app/consult.html')

def consulta_votacionfacultad(request):
    return render(request, 'app/consulta_votacionfacultad.html')

def consultar_votacionsemestre(request):
    return render(request, 'app/consultar_votacionsemestre.html')

def consultar_mivoto(request):
    return render(request, 'app/consultar-mivoto.html')

def crear_estudiante(request):
    
    return render(request, 'app/crear-estudiante.html')

def crear_estudiante2(request):
    try:
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        documento = request.POST['documento']
        semestre = request.POST['semestre']
        email = request.POST['email']

        id_usuario=request.user.id
        facultad=Decano.objects.get(user_id=id_usuario)

        u = User()
        u.first_name=nombre
        u.last_name = apellidos
        u.email = email
        u.username = email
        u.password = documento
        u.save()

        estudiante=Estudiante()

        estudiante.semestreActual=semestre
        estudiante.user_id=u.id
        estudiante.facultad_id=facultad.id
        estudiante.documento=documento
        estudiante.save()
        return redirect('app:lista_estudiantes')
    except:
        veri=True
        return render(request,'app/lista_estudiantes.html')


def crear_votacion(request):
    return render(request, 'app/crear_votacion.html')

def crear_votacion2(request):
    try:
        nombrev = request.POST['nombrev']
        fecha = request.POST['fecha']
        fecha2 = request.POST['fecha2']
        facultad = request.POST['facultad']

        id_usuario=request.user.id
        facultad=Decano.objects.get(user_id=id_usuario)

        v = votacion()
        v.nombre = nombrev
        v.fechaInicio = fecha
        v.fechaFinal = fecha2
        v.tipo_id = facultad
        v.save()

        return redirect('app:crear_votacion')
    except:
        veri=True
        return render(request,'app/votacion-creada.html')

def est(request):
    return render(request, 'app/est.html')

def hacer_votacion(request):
    return render(request, 'app/hacer_votacion.html')

def hacervotacion_facultad(request):
    return render(request, 'app/hacervotación_facultad.html')

def ingresar(request):
    return render(request, 'app/ingresar.html')

def lista_estudiantes(request):
    # id_usuario=request.user.id
    # idd = Decano.objects.get(facultad_id=id_usuario)
    # lista = Estudiante.objects.filter(facultad_id = idd)
    lista = User.objects.all()
    print(lista)
    contexto ={
        'lista_estudiantes':lista,
    }

    return render(request, 'app/lista_estudiantes.html',contexto)

def listade_votaciones_est(request):
    return render(request, 'app/listade-votaciones-est.html')

def listade_votaciones(request):
    return render(request, 'app/listade-votaciones.html')

def listadecandidatos_vot(request):
    return render(request, 'app/listadecandidatos-vot.html')

def menu_estudiante(request):
    return render(request, 'app/menu_estudiante.html')

def postularestudiante(request):
    return render(request, 'app/postularestudiante.html')

def postularse(request):
    return render(request, 'app/postularse.html')

def resultados_finales(request):
    return render(request, 'app/resultados_finales.html')

def resultadosfinales_estudiantes(request):
    return render(request, 'app/resultadosfinales-estudiantes.html')

def ustedse_postulo(request):
    return render(request, 'app/ustedse-postulo.html')

def vot(request):
    return render(request, 'app/vot.html')

def votacion_creada(request):
    return render(request, 'app/votacion-creada.html')

def voto_realizado(request):
    return render(request, 'app/voto_realizado.html')
#-------------------------------------------------------------------

def form_login(request):
    return render(request, 'app/ingresar.html')

def autenticar(request):
    # Obtiene los datos del formulario de autenticación
    username = request.POST['username']
    password = request.POST['password']

    # Obtiene el usuario
    usuario = authenticate(username=username, password=password)

    # Verifica si el usuario existe en la base de datos 
    if usuario is not None:
        # Inicia la sesión del usuario en el sistema
        login(request, usuario)
        # Redirecciona a una página de éxito
        return redirect('app:menu_decano')
    else:
        # Retorna un mensaje de error de login no válido
        return render(request, 'app/ingresar.html') 


def view_logout(request):
  # Cierra la sesión del usuario
  logout(request)
  # Redirecciona la página de login
  return redirect('app:ingresar')



   
