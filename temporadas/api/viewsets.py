from rest_framework.viewsets import ModelViewSet
from temporadas.models import Temporada
from temporadas.api.serializers import TemporadaSerializer


class TemporadaViewSet(ModelViewSet):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer
