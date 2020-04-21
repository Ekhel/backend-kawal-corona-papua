from ..models import Penderita, Kabupaten, Rumah_sakit, Info
from rest_framework import viewsets, filters
from .serializers import PenderitaSerializers, KabupatenSerializers, RsSerializers, InfoSerializers, PapanInfoSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count
from django.db import models

class PenderitaViewSet(viewsets.ReadOnlyModelViewSet):
    search_fields = ['status']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PenderitaSerializers
    queryset = Penderita.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class KabupatenViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = KabupatenSerializers
    queryset = Kabupaten.objects.all()
        
class RsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RsSerializers
    queryset = Rumah_sakit.objects.all()

class InfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InfoSerializers
    queryset = Info.objects.all()

class PapanInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PapanInfoSerializers
    queryset = Info.objects.order_by('-tanggal')[:1]