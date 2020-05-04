from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.db.models import Q, Count
from django.contrib.auth.models import User
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

class Penderita(models.Model):
    id_penderita = models.AutoField(primary_key=True)
    nomor = models.CharField(max_length=10, blank=True)
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
    rs = models.ForeignKey(Rumah_sakit, on_delete=models.CASCADE, default='1')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES,default='sembuh')
    akun_login_pen = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id_penderita',)

    def __str__(self):
        return self.nama_lengkap


class Info(models.Model):
    id_item = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    odp = models.CharField(max_length=20)
    pdp = models.CharField(max_length=20)
    positif = models.CharField(max_length=20)
    sembuh = models.CharField(max_length=20)
    meninggal = models.CharField(max_length=20)
    keteranga = models.TextField()

    class Meta:
        ordering = ('id_item',)
    
    def __str__(self):
        return self.odp

class Odp(models.Model):
    id_odp = models.AutoField(primary_key=True)
    no = models.CharField(max_length=10)
    nama_orang = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('Laki-Laki','LAKI-LAKI'),
        ('Perempuan', 'PEREMPUAN'),
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES,default='laki-laki')
    umur = models.CharField(max_length=10, blank=True)
    alamat = models.CharField(max_length=250)
    no_kontak = models.CharField(max_length=20)
    mulai_dp = models.DateField(auto_now=False)
    berakhir_dp = models.DateField(auto_now=False)
    lokasi = models.ForeignKey(Kabupaten, on_delete=models.CASCADE)

    STATUS_ODP = (
        ('Selesai','SELESAI'),
        ('Belum','BELUM')
    )

    status_opd = models.CharField(max_length=15, choices=STATUS_ODP, default='Belum')
    akun_login_odp = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id_odp',)

    def __str__(self):
        return self.nama_orang


class Pdp(models.Model):
    id_pdp = models.AutoField(primary_key=True)
    no = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('Laki-Laki','LAKI-LAKI'),
        ('Perempuan', 'PEREMPUAN'),
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES,default='laki-laki')
    umur = models.CharField(max_length=10, blank=True)
    alamat = models.CharField(max_length=250)
    no_kontak = models.CharField(max_length=20)
    rs = models.ForeignKey(Rumah_sakit, on_delete=models.CASCADE)
    lokasi = models.ForeignKey(Kabupaten, on_delete=models.CASCADE)

    STATUS_PDP = (
        ('Positif','POSITIF'),
        ('Negatif', 'NEGATIF'),
    )

    status_pdp = models.CharField(max_length=15, choices=STATUS_PDP, default='Negatif')
    akun_login_pdp = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id_pdp',)

    def __str__(self):
        return self.nama

