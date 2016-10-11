from __future__ import unicode_literals
from account.models import AccountUser
from django.db import models


# Create your models here.

class Curriculum(models.Model):
    teacher= models.ManyToManyField(AccountUser, related_name='teacher')
    student = models.ManyToManyField(AccountUser, related_name='student')
    name = models.CharField(max_length=200)
    time = models.DateTimeField('Holding time')
    position = models.CharField(max_length=300)
    content = models.TextField()
    type = models.IntegerField()
    groupID = models.CharField(max_length=255, default="")


# Create your models here.
