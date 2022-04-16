from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('vamos a comerrers')


def categorias(request):
    contexto = {
        'titulo': 'Blockbuster',
        'holabb': 'hola guapoooo',
        'categorias': [
            {'id': 1, 'nombre': 'die hard'},
            {'id': 2, 'nombre': 'lethal weapon'},
        ],
    }
    return render(request, 'app/categorias.html',contexto) #para dibujar la pagina

def peliculas(request):
    return HttpResponse('las pelicuals')

def categoria(request, id):
    numeros = [1, 2, 3]
    print(id)
    print(numeros)
    return HttpResponse(f'Esta es la categoria {id}')

def menu_decano(request):
    return render(request, 'app/menu_decano.html')

def cambiar_estado(request):
    return render(request, 'app/cambiar_estado.html')

def candidatos_ganadores(request):
    return render(request, 'app/candidatos-ganadores.html')

def candidatos_ganadores2(request):
    return render(request, 'app/candidatos-ganadores2.html')

def categorias(request):
    return render(request, 'app/categorias.html')

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
    return render(request, 'app/crear_estudiante.html')

def crear_votacion(request):
    return render(request, 'app/crear_votacion.html')

def est(request):
    return render(request, 'app/est.html')

def hacer_votacion(request):
    return render(request, 'app/hacer_votacion.html')

def hacervotacion_facultad(request):
    return render(request, 'app/Hacervotación_facultad.html')

def ingresar(request):
    return render(request, 'app/ingresar.html')

def lista_estudiantes(request):
    return render(request, 'app/lista_estudiantes.html')

def listade_votaciones_est(request):
    return render(request, 'app/Listade-votaciones.html')

def listade_votaciones(request):
    return render(request, 'app/Listade-votaciones-est.html')

def listadecandidatos_vot(request):
    return render(request, 'app/listadecandidatos-vot.html')

def Menu_estudiante(request):
    return render(request, 'app/Menu_estudiante.html')

def postularestudiante(request):
    return render(request, 'app/postularestudiante.html')

def postularse(request):
    return render(request, 'app/postularse.html')

def Resultados_finales(request):
    return render(request, 'app/Resultados_finales.html')

def resultadosfinales_estudiantes(request):
    return render(request, 'app/resultadosfinales-estudiantes.html')

def Ustedse_postulo(request):
    return render(request, 'app/Ustedse-postulo.html')

def Vot(request):
    return render(request, 'app/Vot.html')

def votacion_creada(request):
    return render(request, 'app/votación-creada.html')

def voto_realizado(request):
    return render(request, 'app/voto_realizado.html')