from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors["title"] = ("Invalid Title, Title must be at least 2 characters")
        if len(post_data['network']) < 3:
            errors["network"] = ("Invalid Network, Network must be at least 3 characters")
        if post_data['released'] == '':
            errors["released"] = ("Invalid Date, Date must be numbers only")
        date = datetime.strptime(post_data['released'], "%Y-%m-%d")
        if date > datetime.now():
            errors["released"] = ('Invalid Date, Date must be in the Past')
        if len(post_data['desc']) != 0 and len(post_data['desc']) < 10:
            errors['desc'] = ('Invalid Description, Description must be at least 10 Characters')
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    released = models.DateTimeField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

















