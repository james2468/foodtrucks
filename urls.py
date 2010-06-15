from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('ftruck.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
)
