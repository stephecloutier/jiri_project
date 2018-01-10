from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    profile_pic = models.FileField(upload_to='uploads/users/', default='default-pic.png')
    is_admin = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profile_pic = models.FileField(upload_to='uploads/students/', default='default-pic.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

