from django.shortcuts import render_to_response
from ftruck.models import Restaurant

def mainmap(request):
    """ render a map with the current location of trucks """

    updates = [r.updates.latest() for r in Restaurant.objects.all()]

    retval = []
    for r in Restaurant.objects.all():
        update = r.latest_geocoded_update()
        if update:
            retval.append({'name': r.name,
                           'avatar': r.avatar,
                           'update': update.update,
                           'website': r.website,
                           'location': update.location})

    return render_to_response('main.html', {'trucks':retval, 'updates': updates})
