# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    name_school = models.CharField(max_length=50)
    name_director = models.CharField(max_length=50)
    address_school = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name_school)


class Student(models.Model):
    name_student = models.CharField(max_length=50)
    surname_student = models.CharField(max_length=50)
    school_student = models.CharField(max_length=50)
    age_student = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.name_student, self.surname_student)


class Teacher(models.Model):
    name_teacher = models.CharField(max_length=50)
    surname_teacher = models.CharField(max_length=50)
    school_teacher = models.CharField(max_length=50)
    age_teacher = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.name_teacher, self.surname_teacher)


# class Bookmarks(models.Model):
#     name_school = models.CharField(max_length=50)
#     name_student = models.CharField(max_length=50)
#

# class Marks(models.Model):
#     subject = models.CharField(max_length=30)
#     value = models.IntegerField()
