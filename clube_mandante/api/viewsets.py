from rest_framework.viewsets import ModelViewSet
from clube_mandante.models import ClubeMandante
from clube_mandante.api.serializers import ClubeMandanteSerializer


class ClubeMandanteViewSet(ModelViewSet):
    queryset = ClubeMandante.objects.all()
    serializer_class = ClubeMandanteSerializer
