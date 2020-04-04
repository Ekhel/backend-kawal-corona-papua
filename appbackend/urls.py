from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . views import (
    KabupateView,
    PenderitaView,
    PenderitaCreateView,
    PenderitaUpdateView,
    RumahSakitView,
    RumahSakitCreateView,
    RumahSakitUpdateView,
    InfoView,
    InfoCreateView,
    InfoUpdateView
)

from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('kabupaten', login_required(KabupateView.as_view()), name='kabupaten'),
    path('penderita', login_required(PenderitaView.as_view()), name='penderita'),
    path('penderita/create', login_required(PenderitaCreateView.as_view()), name='create-penderita'),
    path('penderita/update/<int:pk>', login_required(PenderitaUpdateView.as_view()), name='update-penderita'),
    path('rumahsakit', login_required(RumahSakitView.as_view()), name='rumahsakit'),
    path('rumahsakit/create', login_required(RumahSakitCreateView.as_view()), name='create-rumahsakit'),
    path('rumahsakit/update/<int:pk>', login_required(RumahSakitUpdateView.as_view()), name='update-rumahsakit'),
    path('info', login_required(InfoView.as_view()), name='info'),
    path('info/create', login_required(InfoCreateView.as_view()), name='create-info'),
    path('info/update/<int:pk>', login_required(InfoUpdateView.as_view()), name='update-info'),
]