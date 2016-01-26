from django.db import models
from account.models import AccountUser

class Organization(models.Model):
    name = models.CharField(max_length=100);
    admin = models.ManyToManyField(AccountUser, related_name='admin');
    member = models.ManyToManyField(AccountUser, related_name='member');
    photo = models.ImageField(upload_to="organization");
    website = models.CharField(max_length=100);

# Create your models here.
