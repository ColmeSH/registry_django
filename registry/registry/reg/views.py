# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hi i am index of register application')

def peopleregister(request):
    return HttpResponse('i am the list of italian people')