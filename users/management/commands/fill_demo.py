from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_superuser(username='root', password='root', email='admin@site.local')
        for x in range(1, 5):
            print(f'Creating demo user instance: {x}')
            User.objects.create(
                username=f'test{x}',
                password=f'test{x}',
                email=f'email{x}@site.local',
                first_name=f'Name {x}',
                last_name=f'Surname {x}'
            )
