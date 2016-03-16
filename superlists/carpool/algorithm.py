from bounding_box import BoundingBox, LatLng

debugging = True

# - Compare two Start Locations
# - Compare two End Locations

class RouteAlgorithm(object):	
	# Checks whether the driver and rider route are compatible
	def routes_compatible (self, driver_route, rider_route):
		bounding_box = BoundingBox()
		
		bounding_box.create(
			driver_route.get_start().lat,
			driver_route.get_start().lng,
			driver_route.get_end().lat,
			driver_route.get_end().lng
		)

		# If either part of the route is not in bounds
		if (not bounding_box.in_bounds(
			rider_route.get_start().lat,
			rider_route.get_start().lng) 
			or
			not bounding_box.in_bounds(
			rider_route.get_end().lat,
			rider_route.get_end().lng)):
			print ("Rider route is not in the bounding box")
			return False
		# If the start position of the rider is closer to the end position than the start position of the driver
		elif (driver_route.get_start().distance(rider_route.get_start()) > 
			driver_route.get_start().distance(rider_route.get_end())):
			print ("Rider route start position closer to driver end position")
			return False
		# If the end position of the rider is closer to the start position than the end position of the driver
		elif (driver_route.get_end().distance(rider_route.get_end()) > 
			driver_route.get_end().distance(rider_route.get_start())):
			print ("Rider route end position closer to driver start position")
			return False
		else:
			return True




class Route(object):
	def __init__ (self, start_pos, end_pos, date=None):
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
		
		route_as_string = "Route: " + str(self.start_pos) + " to " + str(self.end_pos)
		if (self.date != None):
			 route_as_string += " on " + str(self.date)
		return route_as_string

# TODO: - Calculate Detour Time/Added Time to Pick up User


# Debugging test for class
if (debugging):
	start_pos = LatLng(5, 5)
	end_pos = LatLng(-5, -5)
	
	driver_route = Route(start_pos, end_pos)

	start_pos = LatLng(3, 3)
	end_pos = LatLng(-3, -3)

	rider_route = Route(start_pos, end_pos)

	algorithm = RouteAlgorithm()

	print (
		algorithm.routes_compatible(
			driver_route,
			rider_route
		)
	)
