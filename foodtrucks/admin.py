from django.contrib.gis import admin
from foodtrucks.models import Restaurant, Update

admin.site.register(Restaurant, admin.GeoModelAdmin)
admin.site.register(Update, admin.GeoModelAdmin)
