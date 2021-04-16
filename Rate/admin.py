from django.contrib import admin

from .models import ServiceBid, TaximeterTarif, TaximeterValue

# admin.site.register(ServiceBid)
# admin.site.register(TaximeterTarif)
# admin.site.register(TaximeterValue)

@admin.register(ServiceBid)
class ServiceBidAdmin(admin.ModelAdmin):
    list_display = ('code_bid', 'driver', 'time_start', 'time_end')

@admin.register(TaximeterTarif)
class TaximeterTarifAdmin(admin.ModelAdmin):
    list_display = ('code_parameter', 'price', 'parameter_unit')

@admin.register(TaximeterValue)
class TaximeterValueAdmin(admin.ModelAdmin):
    list_display = ('code_bid', 'code_parameter')

