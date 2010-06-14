from django.contrib.gis import admin
from ftruck.models import Restaurant, Update

admin.site.register(Restaurant, admin.GeoModelAdmin)
admin.site.register(Update, admin.GeoModelAdmin)
