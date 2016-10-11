from django.db import models
from account.models import AccountUser
from activity.models import Activity

class SignInEvent(models.Model):
    time = models.DateTimeField('Holding time')
    type = models.IntegerField()
    groupID = models.CharField(max_length=255, default="")
    participant = models.ManyToManyField(AccountUser, related_name='participant')
    activity = models.ForeignKey(Activity,default=None)
# Create your models here.
