# trans.gg
This is a simple category-based question-and-answer resource site template written in Django.

While this is created for the trans.gg project, it could be used for any kind of resource-finding website.

## Get it running
```sh
# install django in its own environment
python -m venv .env
.env/bin/pip install django
# run migrations and create an admin user
.env/bin/python manage.py migrate
.env/bin/python manage.py createsuperuser
# run the server!
.env/bin/python manage.py runserver
```