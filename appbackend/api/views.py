from ..models import Penderita, Kabupaten, Rumah_sakit, Info
from rest_framework import viewsets
from .serializers import PenderitaSerializers, KabupatenSerializers, RsSerializers, InfoSerializers, PapanInfoSerializers

class PenderitaViewSet(viewsets.ModelViewSet):
    serializer_class = PenderitaSerializers
    queryset = Penderita.objects.all()

class KabupatenViewSet(viewsets.ModelViewSet):
    serializer_class = KabupatenSerializers
    queryset = Kabupaten.objects.all()

class RsViewSet(viewsets.ModelViewSet):
    serializer_class = RsSerializers
    queryset = Rumah_sakit.objects.all()

class InfoViewSet(viewsets.ModelViewSet):
    serializer_class = InfoSerializers
    queryset = Info.objects.all()

class PapanInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PapanInfoSerializers
    queryset = Info.objects.order_by('-tanggal')[:1]