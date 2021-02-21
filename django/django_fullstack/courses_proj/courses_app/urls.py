from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.index),
    path('courses/add_course', views.add_course),
    path('courses/destroy/<int:course_id>', views.destroy),
    path('courses/comment/<int:course_id>', views.comment),
    path('courses/add_comment/<int:course_id>', views.add_comment),
]