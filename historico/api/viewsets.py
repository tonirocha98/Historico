from rest_framework.viewsets import ModelViewSet
from historico.models import Historico
from historico.api.serializers import HistoricoSerializer


class HistoricoViewSet(ModelViewSet):
    serializer_class = HistoricoSerializer
    queryset = Historico.objects.all()
