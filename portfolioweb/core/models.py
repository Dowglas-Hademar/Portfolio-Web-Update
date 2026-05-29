from django.db import models
from django.conf import settings

class Perfil(models.Model):
    
    # Vincula o perfil a um usuario do Django
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil',
        null=True,
        blank=True,
    )
    
    nome = models.CharField(max_length= 100)
    descricao = models.TextField(max_length= 500)
    curso = models.CharField(max_length= 100)
    periodo = models.CharField(max_length= 10)
    email = models.EmailField(max_length= 255)
    git = models.URLField(max_length= 400)
    linkedin = models.URLField(max_length= 400)
    imagem = models.ImageField(upload_to='perfil/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Perfil Pessoal'
        verbose_name_plural = 'Perfis Pessoais' 
    
    def __str__(self):
        return self.nome

# Create your models here.
