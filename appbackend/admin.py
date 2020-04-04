from django.contrib import admin
from .models import Kabupaten, Penderita, Rumah_sakit

class PageKabupaten(admin.ModelAdmin):
    list_display = ('id_kabupaten','nama')
    list_display_links = ('id_kabupaten','nama')
    search_fields = ('id_kabupaten','nama')
    list_per_page = 5


class PagePenderita(admin.ModelAdmin):
    list_display = ('id_penderita','nama_lengkap','lokasi','status','gender','umur')
    list_display_links = ('id_penderita','nama_lengkap','lokasi','status','gender','umur')
    search_fields = ('id_penderita','nama_lengkap','lokasi','status','gender','umur')
    list_per_page = 10

class PageRumahSakit(admin.ModelAdmin):
    list_display = ('id_rs','rumah_sakit','lokasi','lat','lon')
    list_display_links = ('id_rs','rumah_sakit','lokasi','lat','lon')
    search_fields = ('id_rs','rumah_sakit','lokasi','lat','lon')
    list_per_page = 10


admin.site.register(Kabupaten, PageKabupaten)
admin.site.register(Penderita, PagePenderita)
admin.site.register(Rumah_sakit, PageRumahSakit)

