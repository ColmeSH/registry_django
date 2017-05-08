from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/(?P<student_id>[0-9]+)/info/$', views.student_info, name='student_info'),
    url(r'^student/(?P<student_id>[0-9]+)/marks/$', views.student_marks, name='marks'),
    url(r'^description/$', views.description, name='description'),

]
