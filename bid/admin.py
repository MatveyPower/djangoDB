from django.contrib import admin

from .models import Bid, Street, Area, Location

# admin.site.register(Bid)
# admin.site.register(Street)
# admin.site.register(Area)
# admin.site.register(Location)

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('code_bid', 'phone_number', 'landing_area', 'end_landing_area', 'status')

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    pass

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
