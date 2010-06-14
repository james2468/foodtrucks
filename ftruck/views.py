from django.shortcuts import render_to_response
from ftruck.models import Restaurant

def mainmap(request):
    """ render a map with the current location of trucks """

    restaurants = Restaurant.objects.all()

    return render_to_response('mainmap.html',
                              {'restaurants':restaurants})
