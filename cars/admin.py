from django.contrib import admin

from .models import Car, CarBrand, Driver


admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(Driver)