from django.contrib import admin
from .models import Location, City, Country, ZipCode

admin.site.register(Location)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(ZipCode)
