#REGISTRY APPLICATION || Django project

##INSTALLATION:
- virtualenv env
- source env/bin/activate
- pip install Django
- pip freeze > requirements.txt

###Create a project
- $ django-admin startproject myproject

###Verify if it works
- $ python manage.py runserver

###Start your application
- $ python manage.py startapp myapp
 
###View
- edit view.py file --from django.http import HttpResponse
- map the url in urls.py file

##DATABASE SETUP
- python manage.py migrate
or
- python manage.py makemigrations (new models)

###Create models
- edit myapp/models.py file ---> create a class python
- $ python manage.py makemigrations myapp