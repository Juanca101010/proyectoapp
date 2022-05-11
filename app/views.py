from msilib.schema import RadioButton
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import Decano, Facultad, Estudiante, EstadoVotacion, TipoVotacion, Votacion,Candidato, Voto
from django.contrib.auth.decorators import login_required
from django.db.models import Q	
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse('vamos a comerrers')




	
@login_required
def menu_decano(request):
    return render(request, 'app/menu_decano.html')

@login_required
def cambiar_estado(request):
    lista3 = Votacion.objects.all()
    estados = EstadoVotacion.objects.all()
    print(lista3)
    print(estados)
    contexto ={
        'cambiar_estado':lista3,
        'cambiar_estados':estados,
    }
    return render(request, 'app/cambiar_estado.html',contexto)

@login_required
def cambiar_estado2(request):
    est = int(request.POST['estado'])
    nom = request.POST['nombres']
    print(nom)
    print(est)
    print('holaaaa')
    vo = Votacion.objects.get(id=nom)
    e= EstadoVotacion.objects.get(id=est)
    print(vo)
    vo.estado=e
    vo.save()
    return redirect('app:consultar_votacionsemestre')


@login_required
def candidatos_ganadores(request):
    return render(request, 'app/candidatos-ganadores.html')


@login_required
def candidatos_ganadores2(request):
    return render(request, 'app/candidatos-ganadores2.html')

@login_required
def consult_candidatos_es(request):
    return render(request, 'app/consult-candidatos-es.html')

@login_required
def consult_candidatos(request):
    return render(request, 'app/consult-candidatos.html')

@login_required
def consult_estudiante(request):
    return render(request, 'app/consult-estudiante.html')

@login_required
def consult(request):
    return render(request, 'app/consult.html')

@login_required
def consulta_votacionfacultad(request):
    id_usuario=request.user.id
    facultad_decano=Decano.objects.get(user_id=id_usuario)
        
    listaf=Votacion.objects.filter(facultad_id=facultad_decano.id, tipo_id = 1)

    print(listaf)
    contexto ={
        'consultar_votacionfacultad':listaf,
    }
    return render(request, 'app/consulta_votacionfacultad.html',contexto)

@login_required
def consultar_votacionsemestre(request):
    id_usuario=request.user.id
    facultad_decano=Decano.objects.get(user_id=id_usuario)
        
    listav=Votacion.objects.filter(facultad_id=facultad_decano.id, tipo_id =2)
    print(listav)
    contexto ={
        'consultar_votacionsemestre':listav,
    }
    return render(request, 'app/consultar_votacionsemestre.html',contexto)

@login_required
def consultar_mivoto(request):
    return render(request, 'app/consultar-mivoto.html')


@login_required
def crear_estudiante(request):
    
    return render(request, 'app/crear-estudiante.html')

@login_required
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
        u.set_password(documento)
        u.save()

        estudiante=Estudiante()

        estudiante.semestreActual=semestre
        estudiante.user_id=u.id
        print(u.id)
        estudiante.facultad_id=facultad.id
        estudiante.documento=documento
        estudiante.save()
        return redirect('app:lista_estudiantes')
    except Exception as e:
        print(e)
        return render(request,'app/lista_estudiantes.html')


@login_required
def crear_votacion(request):
    return render(request, 'app/crear_votacion.html')

	
@login_required
def crear_votacion2(request):
    try:
        
        nv = request.POST['nombrev']
        fecha1 = request.POST['fecha']
        fecha22 = request.POST['fecha2']
        fa = request.POST['facultad']

        if fa==1:
            t= TipoVotacion.objects.get(id=1)
        else:
            t= TipoVotacion.objects.get(id=2)

        f= Facultad.objects.get(id=1)
        t= TipoVotacion.objects.get(id=1)
        e= EstadoVotacion.objects.get(id=1)

        v = Votacion()
        v.nombre = nv
        v.fechaInicio = fecha1
        v.fechaFinal = fecha22
        v.tipo = t
        v.estado = e
        v.facultad=f
        v.save()

        return redirect('app:listade-votaciones')
    except Exception as e:
        print(e)
        veri=True
        return render(request,'app/listade-votaciones.html')


@login_required
def est(request):
    return render(request, 'app/est.html')


@login_required
def hacer_votacion(request):
    id_usuario=request.user.id
    facultad_estudiante=Estudiante.objects.get(user_id=id_usuario)
        
    lista2=Votacion.objects.filter(facultad_id=facultad_estudiante.facultad_id, tipo_id =1)

    print(lista2)       
    contexto ={
        'listade_votaciones':lista2,
    }
    return render(request, 'app/hacer_votacion.html',contexto)


@login_required
def hacervotacion_facultad(request):
    return render(request, 'app/hacervotación_facultad.html')

def ingresar(request):
    return render(request, 'app/ingresar.html')


@login_required
def lista_estudiantes(request):

    lista = User.objects.filter(is_superuser=False)
    print(lista)
    contexto ={
        'lista_estudiante':lista,
    }

    return render(request, 'app/lista_estudiantes.html',contexto)


@login_required
def listade_votaciones_est(request):
    lista22 = Votacion.objects.all()
   #tipo=Votacion.objects.get(tipo_id=2)
    print(lista22)
    #print(tipo)
    contexto ={
        'listade_votaciones2':lista22,
    }
    return render(request, 'app/listade-votaciones-est.html',contexto)


@login_required
def listade_votaciones(request):

    lista2 = Votacion.objects.all()

    print(lista2)       
    contexto ={
        'listade_votaciones':lista2,
    }

    return render(request, 'app/listade-votaciones.html',contexto)

@login_required
def listadecandidatos_vot(request):
    return render(request, 'app/listadecandidatos-vot.html')


@login_required
def menu_estudiante(request):
    return render(request, 'app/menu_estudiante.html')


@login_required
def postularestudiante(request):
    lista3 = Votacion.objects.all()
    lista4 = User.objects.filter(is_superuser=False)
    print(lista3)
    print(lista4)
    contexto1 ={
        'p1':lista3,
        'p2':lista4,
    }

    return render(request, 'app/postularestudiante.html',contexto1)


@login_required
def postularestudiante2(request):
    nom = request.POST['nombres']
    vot = request.POST['vot']

    c1= Candidato.objects.all()
    semestr = Estudiante.objects.get(user_id=nom)
    vot2 = Votacion.objects.get(id=vot)

    c1.estudiante = semestr.id
    c1.Votacion = vot2
    c1.semestre =  semestr.semestreActual
    c1.save()
    return render(request,'app/postularestudiante.html')


@login_required
def postularse(request):
    listav= Votacion.objects.all()
    print(listav)
    contexto ={
        'postularse':listav,
    }
    return render(request,'app/postularse.html',contexto)

@login_required
def postularse2(request):
    try:
        
        nv = request.POST['propuestas']
        vot = request.POST['vot']
        idest= request.user.id
        idest2= Estudiante.objects.get(user_id=idest)
        semestrea=Estudiante(id=idest2)
        
        c = Candidato()
        c.propuesta = nv
        c.Votacion_id =vot
        c.estudiante=idest2
        c.semestre=semestrea
        c.save()

        return redirect('app:ustedse-postulo')
    except Exception as e:
        print(e)
        veri=True
        return render(request,'app/postularse.html')

@login_required
def resultados_finales(request):
    return render(request, 'app/resultados_finales.html')

@login_required
def resultadosfinales_estudiantes(request):
    return render(request, 'app/resultadosfinales-estudiantes.html')

@login_required
def ustedse_postulo(request):
    return render(request, 'app/ustedse-postulo.html')

@login_required
def vot(request):
    return render(request, 'app/vot.html')

@login_required
def votacion_creada(request):
    return render(request, 'app/votacion-creada.html')

@login_required
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
        if request.user.is_superuser:
            return redirect('app:menu_decano')
        else:
            return redirect('app:menu_estudiante')

    else:
        # Retorna un mensaje de error de login no válido
        return render(request, 'app/ingresar.html') 


def view_logout(request):
  # Cierra la sesión del usuario
  logout(request)
  # Redirecciona la página de login
  return redirect('app:ingresar')



   
