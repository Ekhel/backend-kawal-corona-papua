from rest_framework import serializers
from ..models import Penderita, Kabupaten

class PenderitaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Penderita
        fields = (
            'id_penderita',
            'nama_lengkap',
            'lokasi',
            'gender',
            'status'
        )

class KabupatenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kabupaten
        fields = (
            'id_kabupaten',
            'nama',
            'lon',
            'lat'
        )