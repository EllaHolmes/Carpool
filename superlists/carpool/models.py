from __future__ import unicode_literals
from django.db import models
import datetime
from carpool.bounding_box import BoundingBox, LatLng
from carpool.algorithm import RouteAlgorithm, Route

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

    def get_type (self):
        return self.user_type

    #WARNING: Not functional until Isaiah figures out how to import geopy
    def get_lat_lng_from_address (address):
        geolocator = Nominatim()

        location = geolocator.geocode(address)

        return LatLng (
            location.latitude,
            location.longitude
        )

    def get_start_lat_lng (self):
        return get_lat_lng_from_address(self.start)

    def get_end_lat_lng (self):
        return get_lat_lng_from_address(self.end)

    def get_route (self):
        return Route (
            self.get_start_lat_lng,
            self.get_end_lat_lng
        )

    class Meta:
        abstract = True


# Create your models here.
class Driver(User):
    user_type = models.CharField(max_length=10, default="Driver")

    
class Rider(User):
    user_type = models.CharField(max_length=10, default="Rider")

    def get_suitable_riders (driver):
        # Initializes a new geolocator
        
        driver_route = driver.get_route()

        algorithm = RouteAlgorithm()

        suitable_riders = []

        for rider in Rider.objects.all():
            if (algorithm.routes_compatible(
                driver_route,
                rider.get_route()
            )):
                suitable_riders.append(rider)

        return suitable_users