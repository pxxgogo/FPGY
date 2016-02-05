from django.db import models
from account.models import AccountUser

class Organization(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ManyToManyField(AccountUser, related_name='admin')
    member = models.ManyToManyField(AccountUser, related_name='member')
    description = models.TextField()
    photo = models.ImageField(upload_to="organization")
    type = models.IntegerField()

# Create your models here.
