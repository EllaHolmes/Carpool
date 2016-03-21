from __future__ import unicode_literals
from django.db import models

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
        driver.date = date
        # do something with the book
        return driver

    def __str__ (self):
        return (self.nameLast + split_char + 
            self.nameFirst + split_char + 
            self.start +split_char + 
            self.end + split_char +
             self.date)

    

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
        rider.date = date
        # do something with the book
        return rider

    def __str__ (self):
                return (self.nameLast + split_char + 
            self.nameFirst + split_char + 
            self.start +split_char + 
            self.end + split_char +
             self.date)
