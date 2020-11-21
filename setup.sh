#!/bin/bash 

echo 'Creating Migrations'
python3 manage.py makemigrations
echo 'Migrating Database'
python3 manage.py migrate
echo 'Collecting Static Files'
python3 manage.py collectstatic
echo 'Creating Sponsor and Front Desk Groups'
python3 manage.py create_groups
echo 'Creating SuperUser, please enter credentials to be used'
python3 manage.py createsuperuser

