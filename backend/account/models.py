from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):
    realName = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    studentID = models.CharField(max_length=13)
    photo = models.ImageField(upload_to = "account")
    gender = models.CharField(max_length=2)
    personID = models.CharField(max_length=255, default="")
    mobileOn = models.BooleanField(default=False)
    mobileToken = models.CharField(default="", max_length=32)

# Create your models here.
