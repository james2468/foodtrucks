from django.core.management.base import NoArgsCommand
from django.core.management import call_command

from ftruck.models import *


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        
        Update.objects.all().delete()
        Restaurant.objects.all().delete()
        
        call_command('update_trucks')