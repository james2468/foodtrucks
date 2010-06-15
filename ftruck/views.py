from django.shortcuts import render_to_response
from ftruck.models import Restaurant

def mainmap(request):
    """ render a map with the current location of trucks """

    retval = []
    for r in Restaurant.objects.all():
        update = r.latest_update()
        retval.append({'name': r.name,
                       'avatar': r.avatar,
                       'update': update.update,
                       'website': r.website,
                       'location': update.location})

                       return render_to_response('mainmap.html', {'trucks':retval})


def tweets(request):
    """ render a list of the latest tweets from today """

    updates = [r.updates.latest() for r in Restaurant.objects.all()]
    
    return render_to_response('tweets.html',
                               {'updates': updates})

