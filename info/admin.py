from django.contrib import admin

from .models import *

class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'phone')
    list_display_links = ('id', 'name')


admin.site.register(Guest, GuestAdmin)

