#!/usr/bin/env bash

chown www-data:www-data /var/log

while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
done

python3 manage.py migrate

uwsgi --strict --ini /opt/app/test_drf/uwsgi/uwsgi.ini