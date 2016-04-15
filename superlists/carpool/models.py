from __future__ import unicode_literals
from django.db import models
import datetime
import math
split_char = "_"



class Route(models.Model):
    def create (self, start_pos, end_pos, date=None):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.date = date

    def get_start(self):
        return self.start_pos

    def get_end(self):
        return self.end_pos

    def get_date(self):
        return self.date

    def __str__ (self):
        return str(self.start_pos) + "to" + str(self.end_pos)


class User(models.Model):
    nameFirst = models.TextField(default = '')
    nameLast = models.TextField(default = '')
    start = models.TextField(default = '')
    end = models.TextField(default = '')
    date = models.TextField(default = '')
    route = None

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
        end_geo = LatLng()

        start_geo.create(
            start_geo_arr[0],
            start_geo_arr[1]
        )

        end_geo.create (
            end_geo_arr[0],
            end_geo_arr[1]
        )

        self.route = Route ()

        self.route.create (
            start_geo,
            end_geo
        )

        return self

    def __str__ (self):
        return (self.nameLast + split_char +
            self.nameFirst + split_char +
            self.start +split_char +
            self.end + split_char +
             str(self.date) + split_char + str(self.route))

    def get_type (self):
        return self.user_type

    def get_route (self):
        return self.route

    class Meta:
        abstract = True


# Create your models here.
class Driver(User):
    user_type = models.CharField(max_length=10, default="Driver")


class Rider(User):
    user_type = models.CharField(max_length=10, default="Rider")


class LatLng(models.Model):
    lat = models.DecimalField(decimal_places = 2, max_digits = 5, )
    lng = models.DecimalField(decimal_places = 2, max_digits = 5, )

    def create(self, lat, lng, tag = None):
        self.lat = lat
        self.lng = lng
        self.tag = tag

    # Can add a string that's a tag if need be
    def set_tag(self, tag):
        self.tag = tag

    def set_lat(self, lat):
        self.lat = lat

    def set_lng(self, lng):
        self.lng = lng

    def get_lat_tag (self):
        return self.get_tag_param(1)

    def get_lng_tag (self):
        return self.get_tag_param(0)

    def get_tag_param (self, param_index):
        return self.tag.split(split_char)[param_index]

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

        if (self.tag != None):
            lat_lng_as_string += " Tag: " + self.tag

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
