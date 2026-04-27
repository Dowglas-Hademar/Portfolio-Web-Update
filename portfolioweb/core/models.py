from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length= 100)
    descricao = models.TextField(max_length= 500)
    curso = models.CharField(max_length= 100)
    periodo = models.CharField(max_length= 10)
    email = models.EmailField(max_length= 255)
    git = models.URLField(max_length= 400)
    linkedin = models.URLField(max_length= 400)
    imagem = models.ImageField(upload_to='perfil/', null=True, blank=True)
    
    def __str__(self):
        return self.nome

# Create your models here.
