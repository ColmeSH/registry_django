# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def index(request):
    return HttpResponse('ciao io sono la index page del sito libretto voti')
