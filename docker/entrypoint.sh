#!/bin/sh
python manage.py makemigrations --settings=gym_project.settings.prod --no-input
python manage.py migrate --settings=gym_project.settings.prod --no-input
python manage.py collectstatic --settings=gym_project.settings.prod --no-input
python manage.py createsuperuser \
        --settings=gym_project.settings.prod --no-input

gunicorn gym_project.wsgi:application --bind 0.0.0.0:8000
