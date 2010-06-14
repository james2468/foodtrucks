from django.core.management.base import NoArgsCommand

from foodtrucks.models import Restaurant, Update

class Command(NoArgsCommand):

    def handle_noargs(self, **options):

        


