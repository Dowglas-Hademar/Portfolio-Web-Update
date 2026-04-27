from django.db import models

# Create your models here.
class Certificado(models.Model):
    descricao = models.TextField(max_length=500)
    
    def __str__(self):
        return self.descricao
    

class Projeto(models.Model):
    tipo = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    git = models.URLField(max_length=255)
    
    def __str__(self):
        return self.nome
