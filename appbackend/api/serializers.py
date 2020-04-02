from rest_framework import serializers
from ..models import Penderita, Kabupaten, Rumah_sakit

class PenderitaSerializers(serializers.ModelSerializer):
    lokasi = serializers.StringRelatedField(read_only=True)

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

class RsSerializers(serializers.ModelSerializer):
    lokasi = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Rumah_sakit
        fields = (
            'id_rs',
            'rumah_sakit',
            'lokasi',
            'lat',
            'lon'
        )