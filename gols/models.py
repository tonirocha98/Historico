from django.db import models


class Gol(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome
