from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

class Indicator(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    fact_value = models.FloatField()
    plan_value = models.FloatField()
    month = models.IntegerField()
