from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appbackend.api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth-token', views.obtain_auth_token, name='api-token-auth'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('appbackend.urls')),
]

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.index_title = settings.ADMIN_SITE_INDEX
