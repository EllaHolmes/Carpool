from __future__ import unicode_literals
from django.db import models
import datetime

split_char = "_"

# Create your models here.
class Driver(models.Model):
    nameFirst = models.TextField(default = '')
    nameLast = models.TextField(default = '')
    start = models.TextField(default = '')
    end = models.TextField(default = '')
    date = models.TextField(default = '')

    def create(first_name, last_name, start, end, date):
        driver = Driver()
        driver.nameFirst = first_name
        driver.nameLast = last_name
        driver.start = start
        driver.end = end
        date_string = date.split("/")
        print(date_string)
        driver.date = datetime.date(
            int(date_string[2]),
            int(date_string[0]),
            int(date_string[1])
        )
        # do something with the book
        return driver

    def __str__ (self):
        return (self.nameLast + split_char + 
            self.nameFirst + split_char + 
            self.start +split_char + 
            self.end + split_char +
             str(self.date))

    

class Rider(models.Model):
    nameFirst = models.TextField(default = '')
    nameLast = models.TextField(default = '')
    start = models.TextField(default = '')
    end = models.TextField(default = '')
    date = models.TextField(default = '')

    def create(first_name, last_name, start, end, date):
        rider = Rider()
        rider.nameFirst = first_name
        rider.nameLast = last_name
        rider.start = start
        rider.end = end
        date_string = date.split("/")
        print(date_string)
        rider.date = datetime.date(
            int(date_string[2]),
            int(date_string[0]),
            int(date_string[1])
        )
        # do something with the book
        return rider

    def __str__ (self):
                return (self.nameLast + split_char + 
            self.nameFirst + split_char + 
            self.start +split_char + 
            self.end + split_char +
             str(self.date))
