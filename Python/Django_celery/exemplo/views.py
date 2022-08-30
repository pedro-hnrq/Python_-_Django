from http.client import HTTPResponse
from django.shortcuts import render
from .tasks import minha_tareda

def home(request):
    minha_tareda.dalay()
    return HTTPResponse('<h1>Estou aqui CELERY</h1>')
