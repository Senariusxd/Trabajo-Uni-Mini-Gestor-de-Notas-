from django.db import models


class Grupo(models.Model):
    año = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.año

class Profesor(models.Model):
    id_profesor = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    grupo_año = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(primary_key=True, max_length=255)
    semestre = models.CharField(max_length=255)
    profesor_id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tiene(models.Model):
    estudiante_id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    profesor_id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Asignatura_Estudiante(models.Model):
    estudiante_id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura_name = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nota = models.CharField(max_length=255)

