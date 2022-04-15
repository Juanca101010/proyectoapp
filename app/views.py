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

