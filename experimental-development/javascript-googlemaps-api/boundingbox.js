function init () {
	console.log("hello world");
	sw = google.maps.LatLng(5, 5);
	ne = google.maps.LatLng(10, 10);
	bounds = new google.maps.LatLngBounds(sw, ne);
	console.log(bounds);
	console.log(bounds.contains(new google.maps.LatLng(7, 7)));
	console.log(bounds.contains(new google.maps.LatLng(0, 0)));
}

window.onload = init;