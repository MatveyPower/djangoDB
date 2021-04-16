from django.contrib import admin

from .models import Car, CarBrand, Driver


# admin.site.register(Car)
# admin.site.register(CarBrand)
# admin.site.register(Driver)


def on_the_line(modeladmin, request, queryset):
    queryset.update(status='y')

on_the_line.short_description = "На линии"

def no_the_line(modeladmin, request, queryset):
        queryset.update(status='n')

no_the_line.short_description="Не на линии"


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('have_car', 'callsign', 'lastname', 'status')
    list_filter = ('have_car','status')
    fields = ['callsign', 'lastname', ('date_of_birth', 'work_experience')]
    search_fields = ('callsign', 'lastname')

    actions = [on_the_line, no_the_line]

class DriverInstanceInline(admin.TabularInline):
    model = Driver

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'color', 'state_number')
    inlines = [DriverInstanceInline]

@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    pass