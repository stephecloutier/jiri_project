from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Student, Project, Event, Meeting, Implementation, Score, Performance

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Meeting)
admin.site.register(Implementation)
admin.site.register(Score)
admin.site.register(Performance)