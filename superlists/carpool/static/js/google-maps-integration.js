var START_POS = null;
var END_POS = null;

function parseToLatLng (address, callback) {
  geocoder = new google.maps.Geocoder();
  geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        callback({
          "lat" : results[0].geometry.location.lat(),
          "lng" : results[0].geometry.location.lng()
        });

        console.log(getRoute());
      }
  });
}

function initInputListeners () {
  $('#id_start').bind('focusout', function() {
    var address = $(this).val() // get the current value of the input field.
    parseToLatLng(address, setStart);

  });

  $('#id_end').bind('focusout', function() {
    var address = $(this).val() // get the current value of the input field.
    parseToLatLng(address, setEnd);
  });
}

function setStart (latlng) {
  START_POS = latlng;
  $("#id_start_lat_lng").val(latLngToString(latlng));
}

function setEnd (latlng) {
  END_POS = latlng;
  $("#id_end_lat_lng").val(latLngToString(latlng));
}


function latLngToString (latlng) {
    return "(" + latlng.lat.toString().split('.')[0] + "." + latlng.lat.toString().split('.')[1].substring(0,2) +
    "," + latlng.lng.toString().split('.')[0] + "." + latlng.lng.toString().split('.')[1].substring(0,2) + ")";
}

function getRoute () {
  return {
    "start" : START_POS,
    "end" : END_POS
  };
}

window.onload = initInputListeners;
