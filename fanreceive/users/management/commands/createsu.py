from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='testUser').exists():
            User.objects.create_superuser(
                username='testUser',
                first_name="testname",
                last_name="testsurname",
                email="testUser@gmail.com",
                age=20,
                city="Cracow",
                password='testpassword'
            )
        print('Superuser has been created.')
