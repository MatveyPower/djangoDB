from django.contrib import admin

from .models import Bid, Street, Area, Location

# admin.site.register(Bid)
# admin.site.register(Street)
# admin.site.register(Area)
# admin.site.register(Location)


def completed(modeladmin, request, queryset):
    queryset.update(status=False)

completed.short_description = "Не выполнен"

def not_done(modeladmin, request, queryset):
        queryset.update(status=True)

not_done.short_description="Выполнен"

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('code_bid', 'phone_number', 'landing_area', 'end_landing_area', 'status')
    list_filter = ('landing_area','status')
    search_fields = ('landing_area', 'code_bid')

    actions = [completed, not_done]

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name_street','code_street')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name_area','code_area')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name_area', 'area', 'driver')
