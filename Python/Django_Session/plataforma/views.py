from django.contrib.messages import constants
import usuarios
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import Cliente

@login_required(login_url= '/auth/login')
def home(request):
        # messages.add_message(request, constants.SUCCESS, 'Seja Bem-Vindo')
        if request.method == 'GET':
                form = Cliente()
                return render(request, 'home.html', {'form': form})
        elif request.method == 'POST':
                form = Cliente(request.POST)
                if form.is_valid():
                        nome = form.data['nome']
                        idade = form.data['idade']
                        data = form.data['data']
                        email = form.data['email']
                        return HttpResponse('Formulário enviado')
                else:
                        return render(request, 'home', {'form' : form} )

