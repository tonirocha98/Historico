from django.db import models
# from partidas.models import Partida
from clubes.models import Clube


class ClubePartida(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.DO_NOTHING, null=True, default=0)
    isMandante = models.BooleanField(default=True)
    # partida = models.ForeignKey(Partida, on_delete=models.DO_NOTHING, null=True, default=0)
    # data_fundacao = models.DateTimeField(null=True)
    # estadio = models.ForeignKey(Estadio, on_delete=models.DO_NOTHING, null=True, default=0)
    # jogadores = models.ManyToManyField(Jogador)

    def __str__(self):
        if self.isMandante:
            return "%s - Mandante " % (self.clube.nome)
        else:
            return "%s - Visitante" % (self.clube.nome)

# class ToppingAmount(models.Model):
#
#             REGULAR = 1
#             DOUBLE = 2
#             TRIPLE = 3
#             AMOUNT_CHOICES = (
#                 (REGULAR, 'Regular'),
#                 (DOUBLE, 'Double'),
#                 (TRIPLE, 'Triple'),
#             )
# amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)