from rest_framework.viewsets import ModelViewSet
from gols.models import Gol
from gols.api.serializers import GolSerializer


class GolViewSet(ModelViewSet):
    queryset = Gol.objects.all()
    serializer_class = GolSerializer
