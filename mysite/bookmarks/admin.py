# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Student, Bookmarks, Marks

admin.site.register(Student)
admin.site.register(Bookmarks)
admin.site.register(Marks)
