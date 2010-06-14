from django.core.management.base import NoArgsCommand

from foodtrucks.models import Restaurant, Update
from foodtrucks.utils import geocode

fakes = ['12th and I NW, Washington DC', '19th and N NW, Washington DC',
         'Dupont Circle, Washington DC', "L'Enfant Plaza, Washington DC",
         '22nd and H NW, Washington DC']
import random

class Command(NoArgsCommand):

    def handle_noargs(self, **options):

        for r in Restaurant.objects.all():
            Update.objects.create(restaurant=r, location=geocode(random.choice(fakes)))

