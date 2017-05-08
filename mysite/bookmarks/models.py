# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Bookmarks(models.Model):
    name_school = models.CharField(max_length=50)
    name_director = models.CharField(max_length=30)


class Marks(models.Model):
    subject = models.CharField(max_length=30)


class Student(models.Model):
    name_student = models.CharField(max_length=50)
    surname_student = models.CharField(max_length=50)
    age_student = models.IntegerField()
