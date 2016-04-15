from __future__ import unicode_literals
from django.db import models
import datetime
from geopy.geocoders import Nominatim
from carpool.bounding_box import BoundingBox
from carpool.algorithm import RouteAlgorithm
import math
split_char = "_"

class LatLng(models.Model):
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    lng = models.DecimalField(max_digits=5, decimal_places=2)

    def create(self, lat, lng, tag = None):
        self.lat = lat
        self.lng = lng

    def set_lat(self, lat):
        self.lat = lat

    def set_lng(self, lng):
        self.lng = lng

    def translate (self, delta_lat, delta_lng):
        self.lat += delta_lat
        self.lng += delta_lng

        # Accounts for wrap around
        self.lat = LatLng.wrap_lat(self.lat)
        self.lng = LatLng.wrap_lng(self.lng)

    # Uses pythagorean theorem to determine distance to another pos
    def distance (self, other_lat_lng):
        return math.sqrt(
            math.pow(self.lat - other_lat_lng.lat, 2) +
            math.pow(self.lng - other_lat_lng.lng, 2)
        )

    def __str__(self):
        lat_lng_as_string = (
            "\"lat\": " +
            str(self.lat) +
            ", \"lng\": " +
            str(self.lng)
        )
        return "{" + lat_lng_as_string + "}"

    # LatLng Util Functions
    @staticmethod
    def wrap_lat (lat):
        if (lat > 90):
            return lat - 180
        elif (lat < -90):
            return lat + 180
        else:
            return lat

    @staticmethod
    def wrap_lng (lng):
        if (lng > 180):
            return lng - 360
        elif (lng < -180):
            return lng + 360
        else:
            return lng

class Route(models.Model):
    start_pos = models.OneToOneField (
        LatLng,
        on_delete=models.CASCADE,
        related_name = "start_pos",
        default = None
    )

    end_pos = models.OneToOneField (
        LatLng,
        on_delete=models.CASCADE,
        related_name = "end_pos",
        default = None
    )

    def create (self, start_pos, end_pos, date=None):
        self.start_pos = start_pos
        self.end_pos = end_pos

    def get_start(self):
        return self.start_pos

    def get_end(self):
        return self.end_pos

    def __str__ (self):
        return str(self.start_pos) + "to" + str(self.end_pos)


class User(models.Model):
    nameFirst = models.TextField(default = '')
    nameLast = models.TextField(default = '')
    start = models.TextField(default = '')
    end = models.TextField(default = '')
    date = models.TextField(default = '')
    route_string = models.TextField(default = '')

    def create (self, first_name, last_name, start, end, date, start_geo_arr, end_geo_arr):
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

        start_geo = LatLng()

        start_geo.create(
            start_geo_arr[0],
            start_geo_arr[1]
        )

        # Makes sure this saves to the database
        start_geo.save()

        end_geo = LatLng()

        end_geo.create (
            end_geo_arr[0],
            end_geo_arr[1]
        )

        # Makes sure this saves to the database
        end_geo.save()

        self.route = Route ()

        self.route.create (
            start_geo,
            end_geo
        )

        # Makes sure this saves to the database
        self.route.save()

        self.route_string = str(self.route)

        return self

    def __str__ (self):
        if (self.route == None):
            self.route = self.get_route()

        return (self.nameLast + split_char +
            self.nameFirst + split_char +
            self.start +split_char +
            self.end + split_char +
             str(self.date) + split_char + str(self.route_string))

    def get_type (self):
        return self.user_type

    def get_lat_lng_from_address (self, address):
        geolocator = Nominatim()

        location = geolocator.geocode(address)
        if (location == None):
            print ("Error: " + address + " is not valid")
            return None

        lat_lng = LatLng ()

        lat_lng.create (
            location.latitude,
            location.longitude
        )

        return lat_lng

    def get_start_lat_lng (self):
        return self.get_lat_lng_from_address(self.start)

    def get_end_lat_lng (self):
        return self.get_lat_lng_from_address(self.end)

    def get_route (self):
        return self.route

        if (start_lat_lng == None or end_lat_lng == None):
            print("Route is null")
            return None
        else:
            route = Route()

            route.create (
                start_lat_lng,
                end_lat_lng
            )

            return route

    class Meta:
        abstract = True


# Create your models here.
class Driver(User):
    user_type = models.CharField(max_length=10, default="Driver")

class Rider(User):
    user_type = models.CharField(max_length=10, default="Rider")

    @staticmethod
    def get_suitable_riders (driver):
        # Initializes a new geolocator
        driver_route = driver.get_route()
        algorithm = RouteAlgorithm()

        suitable_riders = []

        for rider in Rider.objects.all():
            rider_route = rider.get_route()
            if (rider_route != None and algorithm.routes_compatible(
                driver_route,
                rider_route
            )):
                suitable_riders.append(rider)
        return suitable_riders
