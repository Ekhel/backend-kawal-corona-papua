from django.contrib import admin
from django.db.models import Q, Count
from django.db import models
from .models import Kabupaten, Penderita, Rumah_sakit, Info, Odp, Pdp

class PageKabupaten(admin.ModelAdmin):
    list_display = ('id_kabupaten','nama','odp','positif','sembuh','meninggal')
    list_display_links = ('id_kabupaten','nama')
    search_fields = ('id_kabupaten','nama')
    list_per_page = 10

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            positif_count=Count('penderita'),
            sembuh_count=Count('penderita',filter=models.Q(penderita__status="Sembuh")),
            meninggal_count=Count('penderita',filter=models.Q(penderita__status="Meninggal")),
            odp_count=Count('odp'),
        )
        return queryset

    def positif(self, obj):
        return obj.positif_count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

    def sembuh(self, obj):
        return obj.sembuh_count

    def meninggal(self, obj):
        return obj.meninggal_count

    def odp(self, obj):
        return obj.odp_count


class PagePenderita(admin.ModelAdmin):
    list_display = ('nomor','nama_lengkap','lokasi','status','gender','umur')
    list_display_links = ('nomor','nama_lengkap','lokasi','status','gender','umur')
    list_filter = ('status', 'lokasi')
    search_fields = ('no','nama_lengkap','lokasi','status','gender','umur')
    list_per_page = 10

class PageRumahSakit(admin.ModelAdmin):
    list_display = ('id_rs','rumah_sakit','lokasi','lat','lon')
    list_display_links = ('id_rs','rumah_sakit','lokasi','lat','lon')
    search_fields = ('id_rs','rumah_sakit','lokasi','lat','lon')
    list_per_page = 10

class PageInfo(admin.ModelAdmin):
    list_display = ('id_item','tanggal','odp','pdp','positif','sembuh','meninggal')
    list_display_links = ('id_item',)
    search_fields = ('tanggal',)
    list_per_page = 10

class PageOdp(admin.ModelAdmin):
    list_display = ('id_odp','nama_orang','gender','alamat','no_kontak','mulai_dp','berakhir_dp','lokasi','status_opd')
    list_display_links = ('id_odp', 'nama_orang', 'alamat','no_kontak')
    list_filter = ('gender', 'lokasi')
    search_fields = ('nama_orang', 'alamat', 'no_kontak')
    list_per_page = 10

class PagePdp(admin.ModelAdmin):
    list_display = ('id_pdp','nama','gender','umur','no_kontak','lokasi','alamat','rs','status_pdp')
    list_display_links = ('id_pdp','nama','gender','umur','no_kontak','lokasi','alamat','rs','status_pdp')
    list_filter = ('gender', 'lokasi')
    search_fields = ('nama_orang', 'alamat', 'no_kontak')
    list_per_page = 10


admin.site.register(Kabupaten, PageKabupaten)
admin.site.register(Penderita, PagePenderita)
admin.site.register(Rumah_sakit, PageRumahSakit)
admin.site.register(Info, PageInfo)
admin.site.register(Odp, PageOdp)
admin.site.register(Pdp, PagePdp)

