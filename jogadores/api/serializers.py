from rest_framework.serializers import ModelSerializer
from jogadores.models import Jogador


class JogadorSerializer(ModelSerializer):
    class Meta:
        model = Jogador
        fields = ('id', 'nome', 'apelido', 'altura', 'peso', 'data_nascimento', 'idade', 'ativo')
