from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from partidas.models import Partida
from partidas.api.serializers import PartidaSerializer


class PartidaViewSet(ModelViewSet):
    serializer_class = PartidaSerializer
    # queryset = Partida.objects.all()

    def get_queryset(self):
     return Partida.objects.all()
     # return Partida.objects.filter(self.ativo=True)
    http_method_names = ['get', 'post']

    # detail | receber parametro via rota
    # true para metodos especificos da partida x

    @action(methods=['post'], detail=True)
    def adicionar_gols(self, request, id):
        gols = request.data['ids']

        partida = Partida.objects.get(id=id)

        partida.jogadores.set(gols)
        partida.save()
        return Response(self)


    # detail | receber parametro via rota
    # false para metodos que agem em todas as partidas
    @action(methods=['post'], detail=False)
    def adicionar(self, request):
        return Response(self)

    # action deve receber objeto de gol ( idPartida, jogador...)
    # @action(methods=['post'], detail=True)
    # def adicionar_gol_partida_VIEW_MODEL(self, request, gol:
    #     return Response(self)

    def list(self, request, *args, **kwargs):
        return super(PartidaViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PartidaViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PartidaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PartidaViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PartidaViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PartidaViewSet, self).destroy(request, *args, **kwargs)