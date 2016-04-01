import math

from carpool.models import LatLng
# Static variables
debugging = False

top_tag = "Top"
bottom_tag = "Bottom"
left_tag = "Left"
right_tag = "Right"
join_char = "_"

top_left_tag = top_tag + join_char + left_tag
top_right_tag = top_tag + join_char + right_tag
bottom_left_tag = bottom_tag + join_char + left_tag
bottom_right_tag = bottom_tag + join_char + right_tag




# Classes
class BoundingBox(object):

    if (debugging):
        print ("Creating a bounding box object...")

    offset_scale = 0.1
    x_offset = 0
    y_offset = 0

    def set_relative_offset_scale(self, offset):
        self.offset_scale = offset


    def set_offset (self, x_offset, y_offset):

        self.x_offset = x_offset
        self.y_offset = y_offset

        if (debugging):
            print ("The offset is (" + str(x_offset) + ", " + str(y_offset) + ")")

    def set_offset_scale(self, start_pos, end_pos):
        self.x_offset = abs(start_pos.lat - end_pos.lat) * self.offset_scale
        self.y_offset = abs(start_pos.lng - end_pos.lng) * self.offset_scale

    def create(self, start_lat, start_lng, end_lat, end_lng):

        # Sets the two points
        self.set_start_pos(start_lat, start_lng)
        self.set_end_pos(end_lat, end_lng)

        # Sets the offset
        self.set_offset_scale(self.start_pos, self.end_pos)

        # Sets the tags on the start and end positions
        self.set_tags()

        # Sets the corners of the bounding box
        self.set_corners()

        if (debugging):
            print("Created " + str(self))

    def set_start_pos(self, lat, lng):

        self.start_pos = LatLng()
        self.start_pos.create(lat, lng)

        if (debugging):
            print("The start position is " + str(self.start_pos))

    def set_end_pos(self, lat, lng):
        self.end_pos = LatLng()
        self.end_pos.create(lat, lng)

        if (debugging):
            print("The end position is " + str(self.end_pos))


    # Sets the tags of the start and end position to indicate their positions
    def set_tags(self):

        self.start_pos.set_tag (
            self.get_corner_tag(
                self.start_pos,
                self.end_pos
            )
        )

        self.end_pos.set_tag(
            self.get_corner_tag(
                self.end_pos,
                self.start_pos
            )
        )

    # Sets the position of the corners of the bounding box
    def set_corners(self):

        self.top_left_corner = self.get_corner (
            top_left_tag
        )

        self.top_right_corner = self.get_corner (
            top_right_tag
        )

        self.bottom_left_corner = self.get_corner (
            bottom_left_tag
        )

        self.bottom_right_corner = self.get_corner (
            bottom_right_tag
        )

    def get_corner(self, tag, x_offset = None, y_offset = None, start_pos = None, end_pos = None):

        if (y_offset == None):
            y_offset = self.y_offset

        if (x_offset == None):
            x_offset = self.x_offset

        if (start_pos == None):
            start_pos = self.start_pos

        if (end_pos == None):
            end_pos = self.end_pos

        position = LatLng()
        position.create(0,0,tag)

        # Fetch the tags for the positions
        self_lat_tag = self.get_lat_tag(tag)
        self_lng_tag = self.get_lng_tag(tag)

        start_lat_tag = start_pos.get_lat_tag()
        start_lng_tag = start_pos.get_lng_tag()

        end_lat_tag = end_pos.get_lat_tag()
        end_lng_tag = end_pos.get_lng_tag()

        # Set the latitude of this corner
        if (self_lat_tag == start_lat_tag):
            position.set_lat(start_pos.lat)

        elif (self_lat_tag == end_lat_tag):
            position.set_lat(end_pos.lat)

        else:
            self.throw_tag_error(self_lat_tag)


        # Sets the longitude of this corner
        if (self_lng_tag == start_lng_tag):
            position.set_lng(start_pos.lng)

        elif (self_lng_tag == end_lng_tag):
            position.set_lng(end_pos.lng)

        else:
            self.throw_tag_error(self_lat_tag)

        position = self.adjust_position_by_offset(position, x_offset, y_offset)

        return position

    def get_top_left_corner (self):
        return self.top_left_corner

    def get_top_right_corner (self):
        return self.top_right_corner

    def get_bottom_left_corner (self):
        return self.bottom_left_corner

    def get_bottom_right_corner (self):
        return self.bottom_right_corner

    def adjust_position_by_offset(self, position, x_offset, y_offset):
        lat_tag = position.get_lat_tag()
        lng_tag = position.get_lng_tag()

        if (lat_tag == right_tag):
            x_offset *= -1

        if (lng_tag == top_tag):
            y_offset *= -1

        position.translate(x_offset, y_offset)

        return position


    def throw_tag_error (self, tag):
        if (debugging):
            print("!!! Unregistered tag: " + tag + "\n -->Returning None")
        return None

    # Pass in two points (the two for the route) and it can compare
    def get_corner_tag (self, this_point, compare_point):
        if (this_point.lng > compare_point.lng):
            lng_tag = bottom_tag
        else:
            lng_tag = top_tag

        if (this_point.lat > compare_point.lat):
            lat_tag = left_tag
        else:
            lat_tag = right_tag

        return lng_tag + join_char + lat_tag

    def get_lat_tag (self, tag):
        return self.get_tag_param(tag, 1)

    def get_lng_tag (self, tag):
        return self.get_tag_param(tag, 0)

    def get_tag_param (self, tag, param_index):
        return tag.split(join_char)[param_index]

    # Static test
    def test_corner_tag (self):
        this_point = LatLng()
        this_point.create(5,5)
        compare_point = LatLng()
        compare_point.create(-5, 10)   
        return self.get_corner_tag(this_point, compare_point)

    def in_bounds (self, x_pos, y_pos):
        bounds_check = (x_pos >= self.top_right_corner.lat and
            x_pos <= self.top_left_corner.lat and
            y_pos >= self.top_right_corner.lng and
            y_pos <= self.bottom_right_corner.lng)


        if (debugging):
            print ("The point " +
                str(x_pos) + ", " + str(y_pos) +
                " is in bounds " +
                str(bounds_check)
            )

        return bounds_check

    def __str__ (self):
        return ("Bounding Box Object. Corners: \n{\n" +
            "\t" + str(self.top_left_corner) + ",\n" +
            "\t" + str(self.top_right_corner) + ",\n" +
            "\t" + str(self.bottom_left_corner) + ",\n" +
            "\t" + str(self.bottom_right_corner) + "\n}")



    # Uses pythagorean theorem to determine distance to another pos
    def distance (self, other_lat_lng):
        return math.sqrt(
            math.pow(self.lat - other_lat_lng.lat, 2) +
            math.pow(self.lng - other_lat_lng.lng, 2)
        )

    def __str__(self):
        lat_lng_as_string = (
            "Lat: " +
            str(self.lat) +
            ", Lng: " +
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


if (debugging):

    bounding_box = BoundingBox()

    bounding_box.set_relative_offset_scale(0.1)

    start_lat = 89
    start_lng = 179
    end_lat = -7
    end_lng = -4.5

    bounding_box.create(start_lat, start_lng, end_lat, end_lng)

    start_pos = LatLng()
    start_pos.create(start_lat, start_lng, bottom_left_tag)
    end_pos = LatLng(end_lat, end_lng, top_right_tag)
    tag = bounding_box.test_corner_tag()
    lat_tag = bounding_box.get_lat_tag(tag)
    lng_tag = bounding_box.get_lng_tag(tag)

    bounding_box.in_bounds(1, 1)
    bounding_box.in_bounds(10, 10)
    bounding_box.in_bounds(-5, -2)

    print (bounding_box.get_bottom_left_corner())
