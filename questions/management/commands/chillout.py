from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.make_lols()

    def make_lols(self):
        print('Sawa top prepod')

