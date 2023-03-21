from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Usuario
from random import randint

# @cache_page(60*1)
def teste(request):
    x = randint(1, 10)
    usuario = Usuario.objects.all()

    return render(request, 'teste.html', {'usuarios': usuario, 'x': x})