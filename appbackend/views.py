from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Kabupaten, Penderita

def login(request):
    return render(request,'auth/login.html')

@login_required
def dashboard(request):
    contex = {
        "page_title": "Dashboard | Backend"
    }
    
    return render(request, 'page/dashboard.html', contex)

class KabupateView(ListView):
    template_name = 'kabupaten/r-kabupaten.html'
    model = Kabupaten

    def page_title(self):
        contex = {
            "page_title": "Kabupaten"
        }
        return render(contex)

class PenderitaView(ListView):
    template_name = 'penderita/r-penderita.html'
    model = Penderita
    


