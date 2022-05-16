from django import forms
from .models import *

class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'