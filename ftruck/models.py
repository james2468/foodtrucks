import datetime

from django.contrib.gis.db import models
import address

class Restaurant(models.Model):
    twitter_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    base_location = models.PointField(null=True)
    website = models.URLField(blank=True)
    avatar = models.URLField()

    objects = models.GeoManager()

    def latest_geocoded_update(self):
        for update in self.updates.order_by('-timestamp'):
            if update.location:
                return update
        return None

        
    @staticmethod
    def create_from_json(json):
        r = Restaurant()
        
        r.name = json['name']
        r.website = json['url']
        r.twitter_id = json['id']
        r.avatar = json['profile_image_url']
        
        r.save()
        
        return r


class Update(models.Model):
    twitter_status_id = models.BigIntegerField("Twitter Status ID", primary_key=True, blank=False)
    restaurant = models.ForeignKey(Restaurant, related_name='updates')
    update = models.CharField(max_length=200)
    url = models.URLField()
    location = models.PointField(null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    objects = models.GeoManager()
    
    def __unicode__(self):
        return u"%s: %s @ %s (%s)" % (self.restaurant.name, self.update, self.timestamp, self.twitter_status_id)

    class Meta:
        get_latest_by='timestamp'
        
    @staticmethod    
    def create_from_json(json):
        u = Update()
        u.update = json['text']
        #u.timestamp = json['created_at']
        u.twitter_status_id = json['id']
        
        try:
            restaurant = Restaurant.objects.get(twitter_id=json['user']['id'])
        except Restaurant.DoesNotExist:
            restaurant = Restaurant.create_from_json(json['user'])

        u.restaurant = restaurant
        
        u.save()

        return u
        

