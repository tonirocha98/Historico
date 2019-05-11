from django.db import models
from clubes.models import Clube


class Jogador(models.Model):
    clubeAtual = models.ForeignKey(Clube, on_delete=models.PROTECT)
    nome = models.TextField()

    def __str__(self):
        return self.nome
