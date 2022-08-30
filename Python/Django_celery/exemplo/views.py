from django.http.response import HTTPResponse
from django.shortcuts import render
from .tasks import minha_tarefa

def home(request):
    minha_tarefa.delav()
    return HTTPResponse('<h1>Estou aqui CELERY</h1>')
