# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Student


def index(request):
    list_students = Student.objects.order_by('id')[:5]
    context = {'list_students': list_students}
    return render(request, 'bookmarks/index.html', context)


def student_info(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'bookmarks/student_info.html', {'student': student})


def student_marks(request, student_id):
    return HttpResponse("here show list of marks or show object bookmarks of student at id: {}".format(student_id))


def description(request):
    return HttpResponse("this is description of the school")
