from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):
    realName = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    major = models.CharField(max_length=100)
    studentID = models.CharField(max_length=13)
    photo = models.ImageField(upload_to = "account")
    gender = models.CharField(max_length=2)
    wechatOpenID = models.CharField(max_length=20)

# Create your models here.
