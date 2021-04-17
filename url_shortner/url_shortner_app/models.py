from django.db import models

# Create your models here.

class Url(models.Model):
    original_url = models.CharField(max_length=100,unique=True)
    short_url = models.CharField(max_length=50)
    status = models.BooleanField(default=1)

