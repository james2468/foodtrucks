from django.conf.urls.defaults import *

urlpatterns = patterns('ftruck.views',
    url(r'^map/', 'mainmap', name='map'),
)
