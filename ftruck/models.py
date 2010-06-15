import datetime

from django.contrib.gis.db import models
import address

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    base_location = models.PointField(null=True)
    website = models.URLField(blank=True)
    twitter_id = models.CharField(max_length=30)
    avatar = models.URLField()

    objects = models.GeoManager()

    def latest_update(self):
        return self.updates.latest()

    @property
    def current_location(self):
        if not hasattr(self, '_current_location'):
            self._current_location = self.updates.latest().location
        return self._current_location
        
    @staticmethod
    def from_json(json):
        r = Restaurant()
        
        r.name = json['name']
        r.website = json['url']
        r.twitter_id = json['id']
        
        return r


class Update(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='updates')
    update = models.CharField(max_length=200)
    url = models.URLField()
    location = models.PointField(null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    twitter_status_id = models.IntegerField("Twitter Status ID", blank=False) # useful for ensuring we get only fresh updates when we query

    objects = models.GeoManager()
    
    def __str__(self):
        return "%s: %s @ %s (%s)" % (self.restaurant.name, self.update, self.timestamp, self.twitter_status_id)

    class Meta:
        get_latest_by='timestamp'
        
    @staticmethod    
    def from_json(json):
        u = Update()
        u.update = json['text']
        #u.timestamp = json['created_at']
        u.twitter_status_id = json['id']
        
        try:
            restaurant = Restaurant.objects.get(twitter_id=json['user']['id'])
        except Restaurant.DoesNotExist:
            restaurant = Restaurant.from_json(json['user'])

        u.restaurant = restaurant
        
        print u
        
        return u
        

