# CSCI3911-2
- 3 users

  - Admin user:
     - creates sponsors account
     - creates front desk account
     - see records of given badges and information about meetings     

  - Sponsor user:
     - creating meetings
       - addings guests to meetings
       - creating a time slot for a meeting

  - Front Desk user:
     - checking people in
       - lookup meeting by timeslots or sponsor name
       - selecting meeting and assigning/unnassigning badge numbers for checkin/checkout


# Requirements:
Python requirements can be installed using pip install -r requirements.txt

run the provided script or 

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver

To create the superuser, you must within the csci3911-2 directory then run python manage.py createsuperuser then follow the instructions. But for the deployed website, there is already a super user created.
Username: beeva
Password: 1