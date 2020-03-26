from django.contrib import admin
from .models import Kabupaten, Penderita

class PageKabupaten(admin.ModelAdmin):
    list_display = ('id_kabupaten','nama')
    list_display_links = ('id_kabupaten','nama')
    search_fields = ('id_kabupaten','nama')
    list_per_page = 5


class PagePenderita(admin.ModelAdmin):
    list_display = ('id_penderita','nama_lengkap','lokasi','status','gender')
    list_display_links = ('id_penderita','nama_lengkap','lokasi','status','gender')
    search_fields = ('id_penderita','nama_lengkap','lokasi','status','gender')
    list_per_page = 10


admin.site.register(Kabupaten, PageKabupaten)
admin.site.register(Penderita, PagePenderita)

