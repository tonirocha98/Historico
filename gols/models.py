from django.db import models
# from partidas.models import Partida
from jogadores.models import Jogador


class Gol(models.Model):
    # partida = models.ForeignKey(Partida, on_delete=models.PROTECT, null=False, default=0)
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT, null=False, default=0)
    data = models.DateTimeField(null=True)
    anulado = models.BooleanField(default=False)
    gol_contra = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
