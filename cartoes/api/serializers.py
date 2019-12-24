from rest_framework.serializers import ModelSerializer
from cartoes.models import Cartao


class CartaoSerializer(ModelSerializer):
    class Meta:
        model = Cartao
        fields = ('id', 'nome')
