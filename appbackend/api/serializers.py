from rest_framework import serializers
from ..models import Penderita, Kabupaten, Rumah_sakit, Info

class PenderitaSerializers(serializers.ModelSerializer):
    lokasi = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Penderita
        fields = (
            'id_penderita',
            'nomor',
            'nama_lengkap',
            'lokasi',
            'gender',
            'status',
            'umur'
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

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = (
            'id_item',
            'tanggal',
            'odp',
            'pdp',
            'positif',
            'sembuh',
            'meninggal',
        )

class PapanInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = (
            'id_item',
            'tanggal',
            'odp',
            'pdp',
            'positif',
            'sembuh',
            'meninggal',
        )