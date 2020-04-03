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
        ('Laki-Laki','LAKI-LAKI'),
        ('Perempuan', 'PEREMPUAN'),
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES,default='laki-laki')
    STATUS_CHOICES = (
        ('Sembuh','SEMBUH'),
        ('Meninggal', 'MENINGGAL'),
        ('Positif', 'POSITIF'),
    )
    umur = models.CharField(max_length=5, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES,default='sembuh')

    class Meta:
        ordering = ('id_penderita',)

    def __str__(self):
        return self.nama_lengkap


class Rumah_sakit(models.Model):
    id_rs = models.AutoField(primary_key=True)
    rumah_sakit = models.CharField(max_length=100)
    lokasi = models.ForeignKey(Kabupaten, on_delete=models.CASCADE)
    lat = models.CharField(max_length=128)
    lon = models.CharField(max_length=120)

    class Meta:
        ordering = ('id_rs',)
    
    def __str__(self):
        return self.rumah_sakit