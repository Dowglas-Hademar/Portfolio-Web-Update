from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Perfil
from .serializers import PessoalSerializer
from rest_framework.parsers import MultiPartParser, FormParser

def home(request):
    # Se voce ja alterou essa view no exercicio anterior, mantenha como esta
    return render(request, 'portfolio/home.html')


class PerfilDetail(generics.RetrieveUpdateAPIView):
    """
    GET   /api/perfil/ → Retorna o perfil do usuario logado
    PUT   /api/perfil/ → Atualiza o perfil completo
    PATCH /api/perfil/ → Atualiza parcialmente
    """
    
    serializer_class = PessoalSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def get_object(self):
        """
        Em vez de buscar pelo pk da URL, busca pelo usuario logado.
        Se o perfil nao existir, cria um vazio automaticamente.
        """
        perfil, created = Perfil.objects.get_or_create(
            usuario=self.request.user,
            defaults={'nome': self.request.user.username},
        )
        return perfil


# Create your views here.
