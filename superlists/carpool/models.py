from __future__ import unicode_literals
from django.db import models
import datetime

split_char = "_"

class User(models.Model):
    nameFirst = models.TextField(default = '')
    nameLast = models.TextField(default = '')
    start = models.TextField(default = '')
    end = models.TextField(default = '')
    date = models.TextField(default = '')

    def create (self, first_name, last_name, start, end, date):
        self.nameFirst = first_name
        self.nameLast = last_name
        self.start = start
        self.end = end
        date_string = date.split("/")
        self.date = datetime.date(
            int(date_string[2]),
            int(date_string[0]),
            int(date_string[1])
        )

        return self

    def __str__ (self):
        return (self.nameLast + split_char + 
            self.nameFirst + split_char + 
            self.start +split_char + 
            self.end + split_char +
             str(self.date))

    class Meta:
        abstract = True


# Create your models here.
class Driver(User):
    user_type = models.CharField(max_length=10, default="Driver")

    

class Rider(User):
    user_type = models.CharField(max_length=10, default="Rider")
