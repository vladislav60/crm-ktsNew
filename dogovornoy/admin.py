from django.contrib import admin

# Register your models here.
from .models import *


class ktsAdmin(admin.ModelAdmin):
    list_display = (
    'dogovor_number', 'object_number', 'klient_name', 'adres', 'telephone', 'itog_oplata', 'iin_bin')
    list_display_links = ('dogovor_number', 'object_number')
    search_fields = ('dogovor_number', 'object_number')


# Регистрация Базы клиентов договорного в админке
admin.site.register(kts, ktsAdmin)
admin.site.register(rekvizity)
admin.site.register(vid_sign)