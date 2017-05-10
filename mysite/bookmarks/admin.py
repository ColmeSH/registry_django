# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Student, School, Teacher

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
