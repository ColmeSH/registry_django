# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Student
from .models import Teacher
from .models import School


def index(request):
    list_students = Student.objects.order_by('id')[:3]
    list_teachers = Teacher.objects.order_by('age_teacher')[::-1]
    context = {
        'list_students': list_students,
        'list_teachers': list_teachers
    }
    return render(request, 'bookmarks/index.html', context)


def student_info(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'bookmarks/student_info.html', {'student': student})


def teacher_info(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'bookmarks/teacher_info.html', {'teacher': teacher})


# def student_marks(request, student_id):
#     return HttpResponse("here show list of marks or show object bookmarks of student at id: {}".format(student_id))


def description(request, school_id):
    # print name_school
    school = get_object_or_404(School, pk=school_id)
    print school.name_director
    context = {
        'name_school': school.name_school,
        'description': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. ',
    }

    return render(request, 'bookmarks/description.html', context)
