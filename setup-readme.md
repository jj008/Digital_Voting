# Steps to setup
* pip install sklearn
* pip install -r requirements.txt
* Create Digital_Voting Database in PostgreSQL.
* Configure Database section in settings.py.
* python manage.py migrate
* Create an account on https://2factor.in and paste api key from your 2factor account in voter/views.py at line 33, 48, 288 and 308 for SMS OTP verification.
* Update email_id and password in settings.py for email OTP verification.
* python manage.py createsuperuser
* python manage.py runserver
* Login to Django Administration page (http://127.0.0.1:8000/admin) and add details of superuser in EC_Admins.
* Navigate to http://127.0.0.1:8000 and Login as admin, add voter and add candidate details and logout.
* Click on Register and fill voter registration form, record and upload video of 5-10 seconds for face recognition.