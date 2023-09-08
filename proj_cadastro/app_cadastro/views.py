from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvar dados da tela para o banco
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    # Exibir todos os usuarios
    usuarios = {
        'usuarios' : Usuario.objects.all() 
    }
    
    # Retorno dos dados para a pagina listaqgem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)