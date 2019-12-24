from django.db import models
# from jogadores.models import Jogador


class Temporada(models.Model):
    ano = models.TextField(default="")
    # melhor_jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT, default=0, null=True )
    # clubes = models.ManyToManyField(Clube, max_length=2)
    # gols = models.ManyToManyField(Gol, max_length=2)
    # clube_mandante = models.ForeignKey(Clube, on_delete=models.PROTECT, default=0)
    # clube_visitante = models.ForeignKey(Clube, on_delete=models.PROTECT, default=0)

    def __str__(self):
        return self.ano
from django.db import models

# Create your models here.
