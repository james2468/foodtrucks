import datetime

from django.contrib.gis.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    base_location = models.PointField(null=True)
    website = models.URLField(blank=True)
    twitter_id = models.CharField(max_length=30)

    objects = models.GeoManager()

    def latest_update(self):
        return self.updates.latest()

    @property
    def current_location(self):
        if not hasattr(self, '_current_location'):
            self._current_location = self.updates.latest().location
        return self._current_location


class Update(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='updates')
    update = models.CharField(max_length=200)
    url = models.URLField()
    location = models.PointField(null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    twitter_status_id = models.IntegerField("Twitter Status ID", max_length=20, blank=False) # useful for ensuring we get only fresh updates when we query

    objects = models.GeoManager()

    class Meta:
        get_latest_by='timestamp'
