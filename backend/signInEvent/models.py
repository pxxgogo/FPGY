from django.db import models
from account.models import AccountUser

class SignInEvent(models.Model):
    time = models.DateTimeField('Holding time')
    type = models.IntegerField()
    groupID = models.CharField(max_length=255, default="")
    participant = models.ManyToManyField(AccountUser, related_name='participant')
# Create your models here.
