from django.core.management import BaseCommand, CommandError
from fields.models import MyFields
from random import randint, choice, random
import datetime
import string
from django.utils import timezone

from sport.models import Sportsman
from user.models import User


class Command(BaseCommand):
    help = 'Create a field object with random values'

    @staticmethod
    def random_str(length=5):
        character_set = string.ascii_letters
        return ''.join(choice(character_set) for i in range(length))

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        a = options['number']
        name = options['name']
        for item in range(a):
            MyFields.objects.create(
                sportsman=Sportsman.objects.get(name=name),
                is_superfield=randint(0, 1),
                field_name=self.random_str(),
                datetime=timezone.now() - datetime.timedelta(minutes=randint(100, 10000000)),
                field_price=round(random() + randint(1, 1000), 2),
                email=self.random_str(randint(5, 15)) + '@' + self.random_str(randint(3, 5)) + '.com',
                field_year=randint(1, 100),
                field_description=self.random_str(randint(5, 20)) + ', ' + self.random_str(10) + '!',
                field_time=datetime.time(randint(0, 23), randint(0, 59), randint(0, 59)),
            )
        return 'Done'
