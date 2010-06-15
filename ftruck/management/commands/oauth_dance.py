from ftruck.oauth_dance import oauth_dance
from django.core.management.base import NoArgsCommand
from ftruck import get_twitter_settings
from settings import *

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        TS = get_twitter_settings()
        oauth_dance(app_name=TS['app_name'], consumer_key=TS['consumer_key'], consumer_secret=TS['consumer_secret'], token_filename=TS['token_filename'])