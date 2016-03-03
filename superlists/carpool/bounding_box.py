# Static variables
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
class BoundingBox():


	def create(self, start_lat, start_lng, end_lat, end_lng):
		# Gets the two points
		self.start = LatLng(start_lat, start_lng)
		self.end = LatLng(end_lat, end_lng)

		start_tag = self.get_corner_tag(self.start, self.end)
		end_tag = self.get_corner_tag(self.end, self.start)

		self.top_left_corner = None
		self.top_right_corner = None
		self.bottom_left_corner = None
		self.bottom_right_corner = None

		if start.lat > end.lat and start.lng > end.lng:
			#top_left_corner = 
			bottom_right_corner = end
			

		# Determines which corners they are


		# Sets them as those two 

	def get_corner(self, tag, offset_x, offset_y, start_pos, end_pos):
		position = LatLng(0, 0, tag)

		# Fetch the tags for the positions
		self_lat_tag = self.get_lat_tag(tag)
		self_lng_tag = self.get_lng_tag(tag)

		start_lat_tag = self.get_lat_tag(start_pos.tag)
		start_lng_tag = self.get_lng_tag(start_pos.tag)

		end_lat_tag = self.get_lat_tag(end_pos.tag)
		end_lng_tag = self.get_lng_tag(end_pos.tag)

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

		# TODO: Modify the corner pos with the offsets
		
		# ---->

		return position

	def throw_tag_error (self, tag):
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
		
	def test_corner_tag (self):
		this_point = LatLng(5, 5)
		compare_point = LatLng(-5, 10)
		return self.get_corner_tag(this_point, compare_point)

	def get_lat_tag (self, tag):
		return self.get_tag_param(tag, 1)		

	def get_lng_tag (self, tag):
		return self.get_tag_param(tag, 0)

	def get_tag_param (self, tag, param_index):
		return tag.split(join_char)[param_index]

class LatLng(object):
	
	def __init__(self, lat, lng, tag = None):
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

	def __str__(self):
		return "Lat: " + str(self.lat) + ", Lng: " + str(self.lng) + " Tag: " + self.tag

bounding_box = BoundingBox()

start_lat = 5
start_lng = 5
end_lat = -5
end_lng = -5
start_pos = LatLng(start_lat, start_lng, bottom_left_tag)
end_pos = LatLng(end_lat, end_lng, top_right_tag)
tag = bounding_box.test_corner_tag()
lat_tag = bounding_box.get_lat_tag(tag)
lng_tag = bounding_box.get_lng_tag(tag)
print ("Here is the top left corner:\n" + str(bounding_box.get_corner(top_left_tag, 0, 0, start_pos, end_pos)) + "\n")