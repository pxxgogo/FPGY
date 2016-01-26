from django.db import models
from organization.models import Organization
from account.models import AccountUser

class Activity(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('Holding date')
    planNum = models.IntegerField()
    currentNum = models.IntegerField()
    sponsorID = models.CharField(max_length=30)
    position = models.CharField(max_length=300)
    summaryContent = models.TextField()
    info =  models.TextField()
    ddl = models.DateTimeField('deadline')
    adminOrganization = models.ForeignKey(Organization)
    participant = models.ManyToManyField(AccountUser)
    inDate = models.BooleanField(default=True)
# Create your models here.
