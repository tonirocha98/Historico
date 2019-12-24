from rest_framework.viewsets import ModelViewSet
from cartoes.models import Cartao
from cartoes.api.serializers import CartaoSerializer


class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
