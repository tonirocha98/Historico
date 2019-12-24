from rest_framework.viewsets import ModelViewSet
from clubes_partidas.models import ClubePartida
from clubes_partidas.api.serializers import ClubePartidaSerializer


class ClubePartidaViewSet(ModelViewSet):
    queryset = ClubePartida.objects.all()
    serializer_class = ClubePartidaSerializer
