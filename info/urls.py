from django.urls import path
from .views import *

urlpatterns = [
    path('', InfoHome.as_view(), name='home'),
    path('guest/', AddGuest.as_view(), name='index'),
    path('guest/<int:guest_id>/', guest_info, name='guest_info'),
]
