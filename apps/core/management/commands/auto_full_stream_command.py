from django.core.management.base import BaseCommand, CommandError
from apps.core import utils


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('params1', nargs='?', type=int)

    def handle(self, *args, **options):
        # Using parameters:
        # print('params1:', options['params1']
        self.stdout.write('[#] Begin execute...')
        try:
            utils.get_data_full_sport_stream()
        except Exception as e:
            print('Error:', e)
        self.stdout.write('[#] DONE!')
