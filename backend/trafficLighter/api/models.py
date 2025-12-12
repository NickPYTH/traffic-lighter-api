from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

