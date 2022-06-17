from django.db import models

# Create your models here.


class Portfolio(models.Model):
    nome = models.CharField(max_length=100)
    comentario = models.CharField(max_length=600)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome[:50]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=64)
    pontuacao = models.IntegerField(max_length=10)





