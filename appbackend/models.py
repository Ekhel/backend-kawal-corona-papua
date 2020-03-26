from django.db import models
from django.shortcuts import reverse
from django.conf import settings

class Kabupaten(models.Model):
    id_kabupaten = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    lon = models.CharField(max_length=128)
    lat = models.CharField(max_length=128)

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ('id_kabupaten',)


class Penderita(models.Model):
    id_penderita = models.AutoField(primary_key=True)
    nama_lengkap = models.CharField(max_length=250)
    lokasi = models.ForeignKey(Kabupaten, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('laki-laki','LAKI-LAKI'),
        ('perempuan', 'PEREMPUAN'),
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES,default='laki-laki')
    STATUS_CHOICES = (
        ('sembuh','SEMBUH'),
        ('meninggal', 'MENINGGAL'),
        ('perawatan', 'PERAWATAN'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES,default='sembuh')

    class Meta:
        ordering = ('id_penderita',)

    def __str__(self):
        return self.nama_lengkap

