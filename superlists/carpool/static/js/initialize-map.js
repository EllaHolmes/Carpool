var debugging = false;

// Initializes a new parser
parser = new PythonDatabaseObjectParser();

// Pulls the SQL Lite string output from the HTML element it's injected into and converts it into a 2D Array of strings
var allRiders = parser.parseObjectArrayAsStringMatrix(document.getElementById("riders").innerHTML, "Rider");

// Converts the 2D string array into a list of users
allRiders = User.parseFromStringArrayMatrix(allRiders);

// Debugs out the users
if (debugging) {
  console.log(allRiders);
}

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: {lat: 39.82, lng: -98.57}
  });
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var geocoder = new google.maps.Geocoder();
  var infoWindow = new google.maps.InfoWindow(), marker, i;
  var bounds = new google.maps.LatLngBounds();

  directionsDisplay.setMap(map);
  calculateAndDisplayRoute(directionsService, directionsDisplay);


  //places riders on the map and labels them 
  for( i = 0; i < allRiders.length; i++ ) { 
		var position = new google.maps.LatLng(allRiders[i].route.start); 
        bounds.extend(position); 
		var marker = new google.maps.Marker({
		position: position, 
		map: map,

        });
		google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infoWindow.setContent(
								'<div class="info_content">' +
								'<h3>' + allRiders[i].firstName + '</h3>' +  
								'<p>'+ allRiders[i].end +'</p>' +
								'</div>');
                infoWindow.open(map, marker);
            }
        })(marker, i));
        // Automatically center the map fitting all markers on the screen
        map.fitBounds(bounds);}}


function calculateAndDisplayRoute(directionsService, directionsDisplay) {

  directionsService.route({
    origin: document.getElementById('startLoc').innerHTML,
    destination: document.getElementById('endLoc').innerHTML,
    travelMode: google.maps.TravelMode.DRIVING
  }, function(response, status) {
    if (status === google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}

var markers = [ //NOTE: Delete this after transitions to user data
        [[37.449885,-122.196584], [37.49, -122.20], "Fed"],
		[[37.666,-122.1965],[37.49,-122.20]]
        ];

