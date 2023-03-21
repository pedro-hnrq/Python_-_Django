from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario
from django.shortcuts import get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages


def home(request):
    email = request.GET.get("email")
    cond = request.GET.get('cond')    

    if "@gmail" not in email:
        messages.add_message(request, constants.ERROR, 'Informe um email do gmail' )
        return render(request, 'home.html')

    usuario = get_object_or_404(Usuario, email=email)

    if cond == '1':
        return render(request, 'home.html')
    else:
        return render(request, 'logar.html')

    # id = request.GET.get('id')
    # if id == '1':
    #     return HttpResponse("Teste")
    # else:
    #     return HttpResponse(status=500)