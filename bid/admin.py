from django.contrib import admin

from .models import Bid, Street, Area, Location

admin.site.register(Bid)
admin.site.register(Street)
admin.site.register(Area)
admin.site.register(Location)
