#!/bin/bash

NAME=""
DJANGODIR=/var/www/.../src
SOCKFILE=/var/www/.../src/home.sock
NUM_WORKERS=1
USER=root
GROUP=root
DJANGO_SETTINGS_MODULE=config.settings
DJANGO_WSGI_MODULE=config.wsgi

echo "Starting $NAME as `whoami` "

#Activate the virtual environment
cd $DJANGODIR
source /var/www/datavoice/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# create the run directory if it does not exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Sart your Django gunicorn
# Programs meant to be run under supervisor 

exec /var/www/datavoice/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
 --name $NAME \
 --workers $NUM_WORKERS \
 --user=$USER --group=$GROUP \
 --bind=0.0.0.0:8001 \
 --log-level=debug \

