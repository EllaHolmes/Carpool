
class BoundingBox():


	def create(self, start_lat, start_lng, end_lat, end_lng):
		# Gets the two points
		self.start = LatLng(start_lat, start_lng)
		self.end = LatLng(end_lat, end_lng)

		self.top_left_corner = None
		self.top_right_corner = None
		self.bottom_left_corner = None
		self.bottom_right_corner = None

		if start.lat > end.lat and start.lng > end.lng:
			

		# Determines which corners they are


		# Sets them as those two 

	def get_offset()




class LatLng(lat, lng):
	self.lat = lat
	self.lng = lng