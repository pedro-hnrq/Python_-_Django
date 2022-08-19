from django.contrib.messages import constants
import usuarios
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
from django.contrib import messages, auth
from django.contrib.auth.models import User



def login(request):
    if request.user.is_authenticated:
      return redirect('/plataforma/home')  
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})
    
def cadastro(request): 
    if request.user.is_authenticated:
      return redirect('/plataforma/home')    
    status = request.GET.get('status')
    return render(request, 'cadastro.html',{'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    # Vai tirar todos os espaços strip()
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'E-mail ou Senha não podem ficar vazior')
        return redirect('/auth/cadastro/')
    
    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Sua senha deve ter no mínimo 8 caracteres')
        return redirect('/auth/cadastro/')

    
    # usuario = Usuario.objects.filter(email = email)
    
    if User.objects.filter(email = email).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse e-mail')
        return redirect('/auth/cadastro/')

    if User.objects.filter(username = nome).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome')
        return redirect('/auth/cadastro/')

    try:                
        usuario = User.objects.create_user(username = nome, email = email, password = senha)
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com Sucesso!')
        return redirect('/auth/login/')
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect('/auth/cadastro/')

def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    # senha = sha256(senha.encode()).hexdigest()

    usuario = auth.authenticate(request, username = nome, password = senha)

    if not usuario:
        messages.add_message(request, constants.WARNING, 'Nome ou Senha inválido')
        return redirect('/auth/login/')
        # return redirect('/auth/login/?status=1')
    else:

        # request.session['status'] = {'logado': True, 'usuario_id': usuario[0].id}
        # request.session['logado'] = True 
        # request.session['usuario_id'] = usuario[0].id    
        auth.login(request, usuario)
        return redirect('/plataforma/home')

def sair(request):
    #clear() apagar tudo que tiver dentro
    #flush() deletar tudo!
    # request.session.flush()
    auth.logout(request)
    messages.add_message(request, constants.WARNING, 'Faça login antes de acessa a plataforma')
    # request.session['logado'] = None
    # request.session['usuario_id'] = None
    

    # Expiração de Tempo em uma senssão
    # return HttpResponse(request.session.get_expiry_date())
    return redirect('/auth/login/')

    # try:
    #     del request.session['logado']
    #     return redirect('/auth/login/')
    # except:
    #     return redirect('/auth/login/?status=3')
