from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.index_title = settings.ADMIN_SITE_INDEX
