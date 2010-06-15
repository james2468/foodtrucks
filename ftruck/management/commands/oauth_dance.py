from ftruck.oauth_dance import oauth_dance
from django.core.management.base import NoArgsCommand
from settings import *

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        try:
            app_name = TWITTER['app_name']
            consumer_key = TWITTER['consumer_key']
            consumer_secret = TWITTER['consumer_secret']
            token_filename = TWITTER['oauth_filename']
        except:
            raise Exception("Twitter application settings not found. Have you specified them in local_settings.py?")

        oauth_dance(app_name=app_name, consumer_key=consumer_key, consumer_secret=consumer_secret, token_filename=token_filename)