from django.db import models
# from clubes.models import Clube


class Jogador(models.Model):
    nome = models.TextField(default='')
    altura = models.DecimalField(null=True, decimal_places=2, max_digits=3, blank=True)
    peso = models.DecimalField(null=True, decimal_places=2, max_digits=4, blank=True)
    idade = models.IntegerField(null=True, default=0)
    apelido = models.TextField(default='', blank=True)
    data_nascimento = models.DateTimeField(null=True, blank=True)
    ativo = models.BooleanField(default=False)
    # perna_boa = models.TextChoices('Direita', 'Esquerda', 'Ambidestro'),
    # clubeAtual = models.ForeignKey(Clube, on_delete=models.PROTECT, null=True, blank=True)
    foto = models.ImageField(upload_to='jogadores', null=True, blank=True)
    # clubes = models.ManyToManyField(Clube)

    def __str__(self):
        return self.nome
