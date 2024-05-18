from django.db import models
from django.utils import timezone

# class Estudiante(models.Model):
#     rut = models.CharField(max_length=50, primary_key=True)
#     apellido = models.CharField(max_length=50)
#     fecha_nac = models.DateField()
#     activo = models.BooleanField(default=False)
#     creacion_registro = models.DateField(default=timezone.now)
#     modificacion_registro = models.DateField(null=True, blank=True)
#     creado_por = models.CharField(max_length=50)

#     def __str__(self):
#         return self.rut
    
# class Estudiante(models.Model):
#     rut = models.CharField(max_length=50, primary_key=True)
#     apellido = models.CharField(max_length=50)
#     fecha_nac = models.DateField()
#     activo = models.BooleanField(default=False)
#     creacion_registro = models.DateField(default=timezone.now)
#     modificacion_registro = models.DateField(null=True, blank=True)
#     creado_por = models.CharField(max_length=50)
#     cursos = models.ManyToManyField('Curso', through='EstudianteCurso')

#     def __str__(self):
#         return self.rut
    
class Estudiante(models.Model):
    rut = models.CharField(max_length=50, primary_key=True)
    # nombre = models.CharField(max_length=50)  # Añadido
    nombre = models.CharField(max_length=50)  # Añadir un valor por defecto
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(default=timezone.now)
    modificacion_registro = models.DateField(null=True, blank=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField('Curso', through='EstudianteCurso')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"    
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    creacion_registro = models.DateField(default=timezone.now)
    modificacion_registro = models.DateField(null=True, blank=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesores = models.ManyToManyField(Profesor, through='CursoProfesor')

    def __str__(self):
        return self.nombre
    
class CursoProfesor(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    
# Se agregó esta clase para tabla intermedia
class EstudianteCurso(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

  
class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        # return self.calle
        return f"{self.calle} {self.comuna}"
