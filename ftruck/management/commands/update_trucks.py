from django.core.management.base import NoArgsCommand
from django.db.models import Max

from ftruck.models import Restaurant, Update
from ftruck.utils import geocode

# various things stolen from Mike Verdone's excellent Twitter wrapper <http://mike.verdone.ca/twitter/>

import urllib2

def _py26OrGreater():
    import sys
    return sys.hexversion > 0x20600f0

if _py26OrGreater():
    import json
else:
    import simplejson as json

def get_new_statuses(user='sbma44', list_name='dc-food-carts', since_id=None):
    if since_id is not None:
        since_id = "&since_id=%d" % since_id
        
    url = 'http://api.twitter.com/1/%s/lists/%s/statuses.json?per_page=200%s' % (user, list_name, since_id)
    req = urllib2.Request(url)

    try:
        handle = urllib2.urlopen(req)
        return json.loads(handle.read())
    except urllib2.HTTPError, e:
        if (e.code == 304):
            return []
        else:
            raise e




class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        
        since = Update.objects.aggregate(Max('twitter_status_id'))['twitter_status_id__max']
        
        for status in get_new_statuses(since_id=since):
            update = Update.from_json(status)
            update.save()
       