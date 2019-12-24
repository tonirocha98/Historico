from rest_framework.viewsets import ModelViewSet
from estadios.models import Estadio
from estadios.api.serializers import EstadioSerializer


class EstadioViewSet(ModelViewSet):
    queryset = Estadio.objects.all()
    serializer_class = EstadioSerializer
