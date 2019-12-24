"""historico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from clubes.api.viewsets import ClubeViewSet
from jogadores.api.viewsets import JogadorViewSet
from partidas.api.viewsets import PartidaViewSet
from estadios.api.viewsets import EstadioViewSet
from historico.api.viewsets import HistoricoViewSet
from gols.api.viewsets import GolViewSet
from temporadas.api.viewsets import TemporadaViewSet
from cartoes.api.viewsets import CartaoViewSet
from assistencias.api.viewsets import AssistenciaViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

# from clube_mandante.api.viewsets import ClubeMandanteViewSet
# from clube_visitante.api.viewsets import ClubeVisitanteViewSet

router = routers.DefaultRouter()
router.register(r'clubes', ClubeViewSet, basename='Clube')
router.register(r'jogadores', JogadorViewSet, basename='Jogador')
router.register(r'partidas', PartidaViewSet, basename='Partida')
router.register(r'estadios', EstadioViewSet)
router.register(r'historicos', HistoricoViewSet)
router.register(r'gols', GolViewSet, basename='Gol')
router.register(r'temporadas', TemporadaViewSet)
router.register(r'cartoes', CartaoViewSet)
router.register(r'assistencias', AssistenciaViewSet)
# router.register(r'clubesMandantes', ClubeMandanteViewSet)
# router.register(r'clubesVisitantes', ClubeVisitanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token-login/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
