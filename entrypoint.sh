#! /bin/sh

create_superuser="
from django.contrib.auth import get_user_model;
from django.db.utils import IntegrityError;
User = get_user_model();
username = 'testUser'
first_name = 'test_name'
last_name = 'test_surname'
password = 'testpassword'
email = 'TestUser@gmail.com'
age = 20
city = 'testCity'
try:
    User.objects.create_superuser(username=username,
                                  first_name=first_name,
                                  last_name=last_name,
                                  email=email,
                                  password=password,
                                  age=age,
                                  city=city);
except IntegrityError:
    print('User "{}" exists already, not created'.format('${DJANGO_SUPERUSER_USERNAME}'));
"

python manage.py makemigrations
python manage.py migrate --run-syncdb
echo "$create_superuser" | python manage.py shell
exec "$@"