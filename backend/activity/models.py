from django.db import models
from organization.models import Organization
from account.models import AccountUser

class Activity(models.Model):
    publishTime = models.DateTimeField('publishing time')
    publisher = models.ForeignKey(AccountUser)
    name = models.CharField(max_length=200)
    date = models.DateTimeField('Holding date')
    position = models.CharField(max_length=300)
    content =  models.TextField()
    adminOrganization = models.ForeignKey(Organization)
    type = models.IntegerField()
# Create your models here.
