from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    print('index request')
    return render(request, "index.html", context)

def add_course(request):
    errors = Course.objects.validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
    else:
        course = Course.objects.create(
            name = request.POST['name']
        )
        description = Description.objects.create(content=request.POST['description'])
        course.description = description
        course.save()

    return redirect('/courses')

def destroy(request, course_id):
    if request.method == 'GET':
        get_course = Course.objects.get(id=course_id)
        context = {
            'course': get_course
        }
        return render(request, "destroy.html", context)

    if request.method == 'POST':
        get_course = Course.objects.get(id=course_id)
        get_course.delete()
        return redirect('/courses')


def comment(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, "comments.html", context)

def add_comment(request, course_id):
    errors = Comment.objects.validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
    else:
        Comment.objects.create(
            comment = request.POST['comment'],
            course = Course.objects.get(id=course_id)
        )
    return redirect(f"/courses/comment/{course_id}")