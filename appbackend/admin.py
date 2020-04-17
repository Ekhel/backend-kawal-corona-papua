from django.contrib import admin
from django.db.models import Count
from .models import Kabupaten, Penderita, Rumah_sakit, Info

class PageKabupaten(admin.ModelAdmin):
    list_display = ('id_kabupaten','nama','jumlah_positif')
    list_display_links = ('id_kabupaten','nama')
    search_fields = ('id_kabupaten','nama')
    list_per_page = 10

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(items_count=Count('penderita'))
        return queryset

    def jumlah_positif(self, Kabupaten):
        return Kabupaten.items_count

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


admin.site.register(Kabupaten, PageKabupaten)
admin.site.register(Penderita, PagePenderita)
admin.site.register(Rumah_sakit, PageRumahSakit)
admin.site.register(Info, PageInfo)

