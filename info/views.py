from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .models import *
# from .utils import *

class InfoHome(ListView):
    model = Guest
    template_name = 'info/home.html'
    extra_context = {'title': 'Home page'}
    context_object_name = 'guests'


class AddGuest(CreateView):
    form_class = AddGuestForm
    template_name = 'info/index.html'
    extra_context = {'title': 'Заполнить форму'}
    success_url = reverse_lazy('home')


def guest_info(request, guest_id):
    return HttpResponse(f'Accept user {guest_id}')


def pageNotFound(request, expection):
    return HttpResponseNotFound('Not found page')