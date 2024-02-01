
from django.contrib import admin
from django.urls import path
from Grupos import views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('admin/', views.admin_view, name='admin_view'),
    path("", views.home, name="home"),
    path('crear_grupo/', views.crear_grupo, name='crear_grupo'),
    path('lista_grupos/', views.lista_grupos, name='lista_grupos'),
    path('agregar_estudiante/<int:grupo_id>/', views.agregar_estudiante, name='agregar_estudiante'),
    path('detalle_grupo/<int:grupo_id>/', views.detalle_grupo, name='detalle_grupo'),
    path('agregar_nota/<int:estudiante_id>/', views.agregar_nota, name='agregar_nota'),
    path('detalle_estudiante/<int:estudiante_id>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('modificar_estudiante/<int:estudiante_id>/', views.modificar_estudiante, name='modificar_estudiante'),
    path('eliminar_estudiante/<int:estudiante_id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('eliminar_grupo/<int:grupo_id>/', views.eliminar_grupo, name='eliminar_grupo'),
    path('agregar_asignatura/', views.agregar_asignatura, name='agregar_asignatura'),
    path('gestor-notas/', views.gestor_notas_view, name='about'),
    path("login/", views.login_view, name="login"),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('asignatura/modificar/<str:nombre>/', views.modificar_asignatura, name='modificar_asignatura'),
    path('asignatura/eliminar/<str:nombre>/', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('eliminar_nota/<int:asignatura_id>/', views.eliminar_nota, name='eliminar_nota'),
    
]
