from django.conf import settings
from django.utils import simplejson
from django.contrib.gis.geos import Point

import urllib

def geocode(location):
    """
        Given a location return a ``Point`` pair.
    """
    params = {
     'q': location,
     'key': settings.GMAPS_KEY,
     'sensor': 'false',
     'output': 'json',
    }
    url = 'http://maps.google.com/maps/geo?%s' % urllib.urlencode(params)

    try:
        resp = urllib.urlopen(url).read()
        resp = simplejson.loads(resp)
        if resp['Status']['code'] == 200:
            pmark = resp['Placemark'][0]
            lon,lat = pmark['Point']['coordinates'][0:2]
            return Point(lat, lon)
        else:
            return None
    except Exception, e:
        return None

