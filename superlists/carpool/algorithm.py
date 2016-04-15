from carpool.bounding_box import BoundingBox
from carpool.models import Rider, Driver, Route, LatLng


debugging = False

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



# Debugging test for class
if (debugging):
    start_pos = LatLng()
    start_pos.create(5, 5)
    end_pos = LatLng()
    end_pos.create(-5, -5)

    driver_route = Route()
    driver_route.create(start_pos,end_pos)

    start_pos = LatLng()
    start_pos.create(3, 3)
    end_pos = LatLng()
    end_pos.create(-3, -3)

    rider_route = Route()
    rider_route.create(start_pos, end_pos)

    algorithm = RouteAlgorithm()

    print (
        algorithm.routes_compatible(
            driver_route,
            rider_route
        )
    )


   # @staticmethod
def get_suitable_riders(driver, filtered_Riders):
        # Initializes a new geolocator
    driver_route = driver.get_route()
    algorithm = RouteAlgorithm()

    suitable_riders = []

    for rider in filtered_Riders:
        rider_route = rider.get_route()
        if (rider_route != None and algorithm.routes_compatible(
            driver_route,
            rider_route
        )):
            suitable_riders.append(rider)
    return suitable_riders
