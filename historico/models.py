from django.db import models
from partidas.models import Partida
from clubes.models import Clube


class Historico(models.Model):
    # partidas = models.TextField(default='')
    # altura = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    # apelido = models.TextField(default='')
    # data_nascimento = models.DateTimeField(null=True)
    # ativo = models.BooleanField(default=False)
    # perna_boa = models.TextChoices('Direita', 'Esquerda', 'Ambidestro')
    clube = models.ForeignKey(Clube, on_delete=models.PROTECT, null=True)
    partidas = models.ManyToManyField(Partida)

    def __str__(self):
        return self.nome
