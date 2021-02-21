from django.db import models
from datetime import datetime
class CourseManager(models.Manager):
    def validator(request, post_data):
        errors = {}
        if len(post_data['description']) < 15:
            errors['description'] = 'Error, Description must be at least 15 characters'
        if len(post_data['name']) < 5:
            errors['name'] = 'Error, Name must be at least 5 Characters'
        return errors

class CommentManager(models.Manager):
    def validator(request, post_data):
        errors = {}
        if len(post_data['comment']) < 5:
            errors['comment'] = 'Error, Comments must be at least 5 Characters'
        return errors

# Create your models here.
class Description(models.Model):
    content = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.OneToOneField(Description, related_name='course', null=True, on_delete=models.CASCADE)

    objects = CourseManager()


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)

    objects = CommentManager()

