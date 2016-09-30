from django.db import models
from organization.models import Organization
from account.models import AccountUser

class Notification(models.Model):
    publishTime = models.DateTimeField('publishing time')
    TerminalDate = models.DateField()
    publisher = models.ForeignKey(AccountUser)
    title = models.CharField(max_length=100)
    content =  models.TextField()
    adminOrganization = models.ForeignKey(Organization)
    type = models.IntegerField()
# Create your models here.
