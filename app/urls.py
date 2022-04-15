from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('index/', views.index, name='index'), 
    path('categorias', views.categorias, name='categorias'), 
    path('categorias/<int:id>/', views.categoria, name='categoria'), 
    path('peliculas/', views.peliculas, name='peliculas'), 
    path('menu_decano/', views.menu_decano, name='menu_decano'), 
    path('consult_candidatos_es/', views.consult_candidatos_es, name='consult_candidatos_es'), 
]