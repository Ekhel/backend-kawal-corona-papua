from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . views import (
    KabupateView,
    PenderitaView,
)

from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('kabupaten', login_required(KabupateView.as_view()), name='kabupaten'),
    path('penderita', login_required(PenderitaView.as_view()), name='penderita'),
]