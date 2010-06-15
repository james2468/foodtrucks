from settings import *

def get_twitter_settings():
    for x in ('consumer_secret', 'oauth_filename', 'consumer_key', 'app_name', 'user_name', 'list_name'):
        if not TWITTER.has_key(x):
            raise Exception("""Twitter application settings missing or incomplete. Have you specified them in local_settings.py? They should look something like this:
            TWITTER = {
                'app_name': 'My Mapping App',
                'consumer_key': 'abcdefghijklmnop',
                'consumer_secret': '1234567890',
                'oauth_filename': 'ftruck/.oauth_token',
                'user_name': 'my-username',
                'list_name': 'my-list-name'
            }
            """)            
    
    return TWITTER
