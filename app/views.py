from django.shortcuts import render

# Create your views here.

def setsession(request):
    #activar la session
    request.session['nombre'] = 'Pepe'
    request.session['apellido'] = 'Grillo'
    request.session['fecha'] = '2023/04/15'
    request.session['edad'] = 20
    cursos = ['Python','Djnago','Ciencia de Datos','SQLite','MySQL','JavaScript']
    request.session['cursos'] = cursos
    return render(request,'app/setsession.html')

def getsession(request):
    #recuparar datos de la variable de session
    #nombre = request.session['nombre']
    nombre = request.session.get('nombre')
    apellido = request.session.get('apellido')
    fecha = request.session.get('fecha')
    edad = request.session.get('edad')
    cursos = request.session.get('cursos')
    contexto = {'nombre':nombre,'apellido':apellido,'fecha':fecha,'edad':edad,'cursos':cursos}
    return render(request,'app/getsession.html',contexto)

def delsession(request):
    #eliminar variable de session
    if 'nombre' in request.session:
        del request.session['nombre']
        del request.session['apellido']
        del request.session['fecha']
        del request.session['edad']
        del request.session['cursos']
    return render(request,'app/delsession.html')
