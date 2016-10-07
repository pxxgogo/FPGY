from django.db import models

class Suggestion(models.Model):
    adviser = models.CharField(max_length=100)
    time = models.DateTimeField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    email = models.EmailField()

# Create your models here.
