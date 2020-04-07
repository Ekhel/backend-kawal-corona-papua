from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Kabupaten, Penderita, Rumah_sakit, Info

def login(request):
    return render(request,'auth/login.html')

@login_required
def dashboard(request):
    contex = {
        'page_title': 'Dashboard',
        'items': Info.objects.all(),
        'info': Info.objects.order_by('-tanggal')[:1]
    }

    return render(request,'page/dashboard.html',contex)

class KabupateView(ListView):
    template_name = 'kabupaten/r-kabupaten.html'
    model = Kabupaten


class PenderitaView(ListView):
    template_name = 'penderita/r-penderita.html'
    model = Penderita

class PenderitaCreateView(CreateView):
    model = Penderita
    template_name = 'penderita/c-penderita.html'
    fields = ('nama_lengkap','lokasi','gender','status','umur')
    success_url = reverse_lazy('penderita')

class PenderitaUpdateView(UpdateView):
    model = Penderita
    template_name = 'penderita/u-penderita.html'
    fields = ('nama_lengkap','lokasi','gender','status','umur')
    success_url = reverse_lazy('penderita')


@login_required
def create_penderita(request):
    contex = {
        "page_title": "Create | Pasien Positif"
    }
    
    return render(request, 'penderita/c-penderita.html', contex)


class RumahSakitView(ListView):
    template_name = 'rumahsakit/r-rumahsakit.html'
    model = Rumah_sakit


class RumahSakitCreateView(CreateView):
    model = Rumah_sakit
    template_name = 'rumahsakit/c-rumahsakit.html'
    fields = ('rumah_sakit','lokasi','lat','lon')
    success_url = reverse_lazy('rumahsakit')


class RumahSakitUpdateView(UpdateView):
    model = Rumah_sakit
    template_name = 'rumahsakit/u-rumahsakit.html'
    fields = ('rumah_sakit','lokasi','lat','lon')
    context_object_name = 'Rumah Sakit'
    success_url = reverse_lazy('rumahsakit')


class InfoView(ListView):
    model = Info
    template_name = 'page/r-info.html'


class InfoCreateView(CreateView):
    model = Info
    template_name = 'page/c-info.html'
    fields = ('tanggal','odp','pdp','positif','sembuh','meninggal','keteranga')
    success_url = reverse_lazy('info')

class InfoUpdateView(UpdateView):
    model = Info
    template_name = 'page/u-info.html'
    fields = ('tanggal','odp','pdp','positif','sembuh','meninggal','keteranga')
    context_object_name = 'Info'
    success_url = reverse_lazy('info')
    


