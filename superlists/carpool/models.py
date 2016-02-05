from django.db import models

# Create your models here.


class User(models.Model):
	name = models.TextField(default = '')
#	first_name = models.CharField(max_length=30)
#	last_name = models.CharField(max_length=30)
#	start_loc = models.CharField(max_length=500)
#	end_loc = models.CharField(max_length=500)
	
#class Driver(User):
#	isDriver = True

#class Rider(User):	
#	isDriver = False