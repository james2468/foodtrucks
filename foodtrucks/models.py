import datetime

from django.contrib.gis.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    base_location = models.PointField(null=True)
    website = models.URLField()
    twitter_id = models.CharField(max_length=30)

    objects = models.GeoManager()

    def latest_update(self):
        return self.updates.latest()

class Update(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='updates')
    update = models.CharField(max_length=200)
    url = models.URLField()
    location = models.PointField(null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    objects = models.GeoManager()
