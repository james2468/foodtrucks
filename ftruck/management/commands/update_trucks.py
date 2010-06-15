import os, urllib2
from django.core.management.base import NoArgsCommand
from django.db.models import Max

# various things stolen from Mike Verdone's excellent Twitter wrapper <http://mike.verdone.ca/twitter/>
from ftruck.api import Twitter 
from ftruck.oauth import *
from settings import *
from ftruck.models import Restaurant, Update
from ftruck.utils import geocode
from ftruck import get_twitter_settings

def get_twitter_api_wrapper():
    token_filename = TWITTER.get('oauth_filename', 'ftruck/.oauth_token')
    if not os.path.exists(token_filename):
        raise Exception("No OAuth token found at %s. Please run the 'oauth_dance' command first." % token_filename)

    TS = get_twitter_settings()

    (token, token_secret) = read_token_file(token_filename)    
    api = Twitter(auth=OAuth(token=token, token_secret=token_secret, consumer_key=TS['consumer_key'], consumer_secret=TS['consumer_secret']), domain='api.twitter.com', api_version='1')
    return api


def get_new_statuses(user=None, list_name=None, since_id=None):
    
    TS = get_twitter_settings()
    if user is None:
        user = TS['user_name']
    if list_name is None:
        list_name = TS['list_name']
    
    api = get_twitter_api_wrapper()

    if since_id is None:        
        statuses = getattr(getattr(api, user).lists, list_name).statuses()
    else:
        statuses = getattr(getattr(api, user).lists, list_name).statuses(since_id=since_id)

    return statuses


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        
        since = Update.objects.aggregate(Max('twitter_status_id'))['twitter_status_id__max']
        
        for status in get_new_statuses(since_id=since):
            update = Update.from_json(status)
            update.save()
       