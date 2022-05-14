from django import forms
from .models import *

class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'



    # name = forms.CharField(max_length=255)
    # mail = forms.EmailField()
    # phone = forms.IntegerField()
    # CPU_vendor = forms.ModelChoiceField(queryset=CPU_Vendors.objects.all(), label='CPU')
    # GPU_vendor = forms.ModelChoiceField(queryset=GPU_Vendors.objects.all(), label='GPU')
    # agree = forms.BooleanField()
