from rest_framework import serializers
from .models import Perfil

class PessoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = [
            'id', 'nome', 'descricao', 'curso',
            'periodo', 'email', 'git', 'linkedin', 'imagem',
        ]