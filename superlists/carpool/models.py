from django.db import models

# Create your models here.
class User(models.Model):
    nameFirst = models.TextField(default = '')
    nameLast = models.TextField(default = '')
    start = models.TextField(default = '')
    end = models.TextField(default = '')
    date = models.TextField(default = '')