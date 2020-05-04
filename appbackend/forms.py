from django import forms
from .models import Odp

class odpCreate(forms.ModelForm):
    class Meta:
        model: Odp
        fields: '__all__'