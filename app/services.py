from .models import Estudiante, Profesor, Curso, Direccion, CursoProfesor
from django.utils import timezone

def crear_curso(codigo, nombre, version):
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, version=version)
    return curso

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, creado_por=creado_por)
    return profesor

def crear_estudiante(rut, apellido, fecha_nac, creado_por):
    estudiante = Estudiante.objects.create(rut=rut, apellido=apellido, fecha_nac=fecha_nac, creado_por=creado_por)
    return estudiante

def crear_direccion(calle, dpto, comuna, ciudad, region, estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    direccion = Direccion.objects.create(calle=calle, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    return direccion

def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def agrega_profesor_a_curso(codigo_curso, rut_profesor):
    curso = Curso.objects.get(codigo=codigo_curso)
    profesor = Profesor.objects.get(rut=rut_profesor)
    CursoProfesor.objects.create(curso=curso, profesor=profesor)

# def agrega_cursos_a_estudiante(rut_estudiante, lista_codigos_cursos):
#     estudiante = Estudiante.objects.get(rut=rut_estudiante)
#     for codigo in lista_codigos_cursos:
#         curso = Curso.objects.get(codigo=codigo)
#         estudiante.curso_set.add(curso)
        
def agrega_cursos_a_estudiante(rut_estudiante, lista_codigos_cursos):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    for codigo in lista_codigos_cursos:
        curso = Curso.objects.get(codigo=codigo)
        estudiante.cursos.add(curso)  # Utiliza el atributo 'cursos'


def imprime_estudiante_cursos(rut_estudiante):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    cursos = estudiante.curso_set.all()
    for curso in cursos:
        print(curso.nombre)

# def obtener_estudiantes_con_direccion_y_cursos():
#     estudiantes = Estudiante.objects.all()
#     resultado = []
#     for estudiante in estudiantes:
#         direccion = Direccion.objects.get(estudiante=estudiante)
#         cursos = estudiante.curso_set.all()
#         resultado.append({
#             'estudiante': estudiante,
#             'direccion': direccion,
#             'cursos': cursos
#         })
#     return resultado

# def obtener_estudiantes_con_direccion_y_cursos():
#     estudiantes = Estudiante.objects.all()
#     resultado = []
#     for estudiante in estudiantes:
#         direccion = Direccion.objects.get(estudiante=estudiante)
#         cursos = estudiante.cursos.all()  # Cambiar curso_set a cursos
#         resultado.append({
#             'estudiante': estudiante,# esto se puede desagregar en todos los campos de estudiantes
#             'direccion': direccion,
#             'cursos': cursos
#         })
#     return resultado

def obtener_estudiantes_con_direccion_y_cursos():
    estudiantes = Estudiante.objects.all()
    resultado = []
    for estudiante in estudiantes:
        direccion = Direccion.objects.get(estudiante=estudiante)
        cursos = estudiante.cursos.all()
        resultado.append({
            'rut': estudiante.rut,
            'nombre': estudiante.nombre,  # Añadido
            'apellido': estudiante.apellido,  # Añadido
            'direccion': f"{direccion.calle}, {direccion.dpto if direccion.dpto else ''}, {direccion.comuna}, {direccion.ciudad}, {direccion.region}",
            'cursos': [curso.nombre for curso in cursos]  # Ajustado para mostrar nombres de los cursos
        })
    return resultado


def obtener_profesores_y_sus_cursos():
    profesores = Profesor.objects.all()
    resultado = []
    for profesor in profesores:
        cursos = profesor.curso_set.all()
        resultado.append({
            'profesor': profesor,
            'cursos': cursos
        })
    return resultado

def obtener_cursos_con_estudiantes_y_profesores():
    cursos = Curso.objects.all()
    resultado = []
    for curso in cursos:
        estudiantes = curso.estudiante_set.all()
        profesores = curso.profesores.all()
        resultado.append({
            'curso': curso,
            'estudiantes': estudiantes,
            'profesores': profesores
        })
    return resultado
