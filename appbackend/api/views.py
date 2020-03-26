from ..models import Penderita, Kabupaten
from rest_framework import viewsets
from .serializers import PenderitaSerializers, KabupatenSerializers

class PenderitaViewSet(viewsets.ModelViewSet):
    serializer_class = PenderitaSerializers
    queryset = Penderita.objects.all()

class KabupatenViewSet(viewsets.ModelViewSet):
    serializer_class = KabupatenSerializers
    queryset = Kabupaten.objects.all()