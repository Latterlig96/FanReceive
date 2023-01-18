#!/bin/bash

set -o errexit  
set -o nounset

export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_PASSWORD="testpassword"
export DJANGO_SUPERUSER_EMAIL="testuser@gmail.com"
export DJANGO_SUPERUSER_FIRST_NAME="user"
export DJANGO_SUPERUSER_LAST_NAME="test"
export DJANGO_SUPERUSER_AGE=20
export DJANGO_SUPERUSER_CITY="Cracow"

exec "$@"