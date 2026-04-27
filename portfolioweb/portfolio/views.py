from django.shortcuts import render
from django.contrib import messages
from core.models import Perfil
from .models import Certificado, Projeto


def home(request):
    perfil = Perfil.objects.all().first()
    certificados = Certificado.objects.all()
    
    return render(request, 'portfolio/home.html', {"perfil" : perfil, "certicados" : certificados})


def projetos(request):
    projetos = Projeto.objects.all()
    
    return render(request, 'portfolio/projetos.html', {"projetos" : projetos})

def contato(request):
    
    if request.method == 'POST':
        messages.success(request, 'Mensagem enviada com sucesso!')
        
    return render(request, 'portfolio/contato.html')