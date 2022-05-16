from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('index/', views.index, name='index'), 
    path('menu_decano/', views.menu_decano, name='menu_decano'), 
    path('cambiar_estado/', views.cambiar_estado, name='cambiar_estado'), 
    path('cambiar_estado2/', views.cambiar_estado2, name='cambiar_estado2'), 
    path('candidatos-ganadores/', views.candidatos_ganadores, name='candidatos-ganadores'), 
    path('candidatos-ganadores2/', views.candidatos_ganadores2, name='candidatos-ganadores2'), 
    path('consult-candidatos-es/', views.consult_candidatos_es, name='consult-candidatos-es'), 
    path('consult-candidatos/', views.consult_candidatos, name='consult-candidatos'), 
    path('consult-estudiante/', views.consult_estudiante, name='consult-estudiante'), 
    path('consult/', views.consult, name='consult'), 
    path('consulta_votacionfacultad/', views.consulta_votacionfacultad, name='consulta_votacionfacultad'), 
    path('consultar_votacionsemestre/', views.consultar_votacionsemestre, name='consultar_votacionsemestre'), 
    path('consultar-mivoto/', views.consultar_mivoto, name='consultar-mivoto'), 
    path('crear-estudiante/', views.crear_estudiante, name='crear-estudiante'),  
    path('crear_estudiante2/', views.crear_estudiante2, name='crear_estudiante2'),  
    path('crear_votacion/', views.crear_votacion, name='crear_votacion'), 
    path('crear_votacion2/', views.crear_votacion2, name='crear_votacion2'), 
    path('est/', views.est, name='est'), 
    path('hacer_votacion/', views.hacer_votacion, name='hacer_votacion'), 
    path('hacervotacion_facultad/', views.hacervotacion_facultad, name='hacervotacion_facultad'), 
    path('ingresar/', views.ingresar, name='ingresar'), 
    path('index/', views.index, name='index'), 
    path('lista_estudiantes/', views.lista_estudiantes, name='lista_estudiantes'), 
    path('listade-votaciones-est/', views.listade_votaciones_est, name='listade-votaciones-est'), 
    path('listade-votaciones/', views.listade_votaciones, name='listade-votaciones'), 
    path('listadecandidatos-vot/', views.listadecandidatos_vot, name='listadecandidatos-vot'), 
    path('menu_estudiante/', views.menu_estudiante, name='menu_estudiante'), 
    path('postularestudiante/', views.postularestudiante, name='postularestudiante'), 
    path('postularestudiante2/', views.postularestudiante2, name='postularestudiante2'), 
    path('postularse/', views.postularse, name='postularse'), 
    path('postularse2/', views.postularse2, name='postularse2'), 
    path('resultados_finales/', views.resultados_finales, name='resultados_finales'), 
    path('resultadosfinales_estudiantes/', views.resultadosfinales_estudiantes, name='resultadosfinales_estudiantes'), 
    path('ustedse-postulo/', views.ustedse_postulo, name='ustedse-postulo'), 
    path('vot/', views.vot, name='vot'), 
    path('votacion-creada/', views.votacion_creada, name='votacion-creada'), 
    path('voto_realizado/', views.voto_realizado, name='voto_realizado'), 


    #---------------------------------------------------------------------------------
    path('ingresar/', views.form_login, name='form_login'), 
    path('autenticar/', views.autenticar, name='autenticar'),   
    path('logout/', views.view_logout, name='view_logout'), 

    #///////////////////////////////////////////////////////////////
    #crear estudiante
]