from ..models import Penderita, Kabupaten, Rumah_sakit
from rest_framework import viewsets
from .serializers import PenderitaSerializers, KabupatenSerializers, RsSerializers

class PenderitaViewSet(viewsets.ModelViewSet):
    serializer_class = PenderitaSerializers
    queryset = Penderita.objects.all()

class KabupatenViewSet(viewsets.ModelViewSet):
    serializer_class = KabupatenSerializers
    queryset = Kabupaten.objects.all()

class RsViewSet(viewsets.ModelViewSet):
    serializer_class = RsSerializers
    queryset = Rumah_sakit.objects.all()