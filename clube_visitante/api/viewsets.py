from rest_framework.viewsets import ModelViewSet
from clube_visitante.models import ClubeVisitante
from clube_visitante.api.serializers import ClubeVisitanteSerializer


class ClubeVisitanteViewSet(ModelViewSet):
    queryset = ClubeVisitante.objects.all()
    serializer_class = ClubeVisitanteSerializer
