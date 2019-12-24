from django.db import models


class Estadio(models.Model):
    nome = models.TextField(default="")
    data_fundacao = models.DateTimeField(null=True)

    def __str__(self):
        return self.nome
