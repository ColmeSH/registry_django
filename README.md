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
- $ python manage.py sqlmigrate myapp 0001 --print SQL in to the screen
- $ python manage.py migrate

###Playing with the API
- $ python magage.py shell
>>> from myapp.models import Bookmarks, Marks, Student
example:
>>> Student.objects.all()   ---> query on student model 
>>> s1 = Student()          ---> create object student