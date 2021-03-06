from django.db import models
from clubes.models import Clube
# from partidas.models import Partida


class ClubeMandante(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.PROTECT, null=True)
    # partida = models.ForeignKey(Partida, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.clube.nome
