from django.conf.urls import url

from . import views

urlpatterns = [

    #Homepage
    url(r'^$', views.index, name='index'),

    #Teacher
    url(r'^teacher/(?P<teacher_id>[0-9]+)/info/$', views.teacher_info, name='teacher_info'),

    #Student
    url(r'^student/(?P<student_id>[0-9]+)/info/$', views.student_info, name='student_info'),
    # url(r'^student/(?P<student_id>[0-9]+)/marks/$', views.student_marks, name='marks'),

    #School
    url(r'^description/(?P<school_id>[0-9]+)/$', views.description, name='description'),

]
