from django.db import models


class Rodada(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome
