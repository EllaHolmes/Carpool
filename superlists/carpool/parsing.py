# Returns the values as length 2 array
def parse_lat_lng_string(lat_lng_string):
  lat_lng_string = lat_lng_string[1:-1]
  lat = float(lat_lng_string.split(",")[0])
  lng = float(lat_lng_string.split(",")[1])
  return [lat, lng]
