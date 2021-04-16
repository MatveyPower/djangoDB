from django.contrib import admin

from .models import ServiceBid, TaximeterTarif, TaximeterValue

admin.site.register(ServiceBid)
admin.site.register(TaximeterTarif)
admin.site.register(TaximeterValue)

