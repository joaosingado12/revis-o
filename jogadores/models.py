from django.db import models

# Create your models here.

class Jogadores(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()
    idade = models.IntegerField()
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    time = models.CharField(max_length=100)
    posicao = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='foto_jogadores', null=True, blank=True)
    descricao = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.nome