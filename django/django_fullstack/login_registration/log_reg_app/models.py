from django.db import models
from datetime import datetime
import re
# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Error! First Name must be at least 2 Characters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Error! Last Name must be at least 2 Characters."
        if not EMAIL_REGEX.match(postData['email_address']):
            errors["email_address"] = "Error! Email must be formatted as name@abc.xyz, Example John23@mail.com"
        if len(postData['password']) < 8:
            errors["password"] = "Error! Password must be at least 8 Characters."
        if not postData['password'] == postData['confirm_password']:
            errors["confirm_password"] = "Error! Your passwords did not match."
        email_check = User.objects.filter(email_address=postData['email_address'])
        if email_check:
            errors["email"] = "Error! Email already registered."
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=55)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
