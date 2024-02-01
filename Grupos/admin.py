from django.contrib import admin
from .models import Grupo, Profesor, Estudiante, Asignatura, Tiene, Asignatura_Estudiante

admin.site.register(Grupo)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Asignatura)
admin.site.register(Tiene)
admin.site.register(Asignatura_Estudiante)