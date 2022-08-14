# Steps to setup
* pip install sklearn
* pip install -r requirements.txt
* Create Digital_Voting Database in PostgreSQL.
* Configure Database section in settings.py.
* python manage.py migrate
* python manage.py createsuperuser
* Login to Django Administration page and add details of superuser in EC_Admins.