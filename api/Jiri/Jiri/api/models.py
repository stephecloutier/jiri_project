from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='uploads/users/', default='default-pic.png')
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password', 'first_name', 'last_name', 'is_admin']
    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='uploads/students/', default='default-pic.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    default_weight = models.DecimalField(max_digits=3, decimal_places=2)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return self.name 


class Event(models.Model):
    PREMIERE = '1'
    SECONDE = '2'
    SESSION_IN_YEAR_CHOICES = (
        (PREMIERE, 'Première'),
        (SECONDE, 'Seconde'),
    )
    course_name = models.CharField(max_length=50)
    exam_session = models.CharField(max_length=1, choices=SESSION_IN_YEAR_CHOICES)
    exam_date = models.DateField()
    projects = models.ManyToManyField('Project')
    students = models.ManyToManyField('Student')
    users = models.ManyToManyField('User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return self.course_name + ' ' + self.exam_date.strftime('%d %B %Y')


class Implementation(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    url_project = models.URLField(blank=True, null=True)
    url_repo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.weight:
              self.weight = self.project.default_weight
        super(Implementation, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.student.id) + ' ' + self.project.name + ' ' + str(self.event.id)


class Meeting(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='meetings')
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return self.user.username + ' ' + str(self.student.id) + ' ' + str(self.event.id)


class Score(models.Model):
    score = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)
    implementation = models.ForeignKey('Implementation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return str(self.meeting.id) + ' ' + str(self.implementation.id)


class Performance(models.Model):
    final_score = models.DecimalField(max_digits=4, decimal_places=2)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return self.student + ' ' + self.event + ' ' + self.final_score