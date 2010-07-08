from django.conf.urls.defaults import *

urlpatterns = patterns('ftruck.views',
    url(r'^$', 'mainmap', name='map'),
    url(r'^tweets/$', 'tweets', name='tweets')
)
