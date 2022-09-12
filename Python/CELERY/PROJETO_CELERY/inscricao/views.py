from re import template
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pessoa
from django.conf import settings
from PIL import Image, ImageDraw
import os

def inscricao(request):
    return render(request, 'inscricao.html')

def processa_inscricao(request):

    def cria_convite(nome, email):
        template = os.path.join(settings.STATIC_ROOT, 'img/pasta.png')
        img = Image.open(template)
        img_escrever = ImageDraw.Draw(img)
        img_escrever.text((40, 270), nome, fill=( 200, 89, 255))
        path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{email}.png')
        img.save(path_salvar)

    cria_convite('Pedro','Pedro ')
    return HttpResponse('teste')
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()
    return HttpResponse('Teste')