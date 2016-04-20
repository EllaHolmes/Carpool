var START_POS = null;
var END_POS = null;

function parseToLatLng (address, latLngCallback, addressCallback) {
  geocoder = new google.maps.Geocoder();
  geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        latLngCallback({
          "lat" : results[0].geometry.location.lat(),
          "lng" : results[0].geometry.location.lng()
        });

        addressCallback(results[0].formatted_address);

        console.log(getRoute());
      }
  });
}

function init () {
    initInputListeners();
    checkForInitialValues();
}
function initInputListeners () {
  $('#id_start').bind('focusout', function() {
    var address = $(this).val() // get the current value of the input field.
    parseToLatLng(address, setStart, setStaticStart);

  });


  $('#id_end').bind('focusout', function() {
    var address = $(this).val() // get the current value of the input field.
    parseToLatLng(address, setEnd, setStaticEnd);
  });
}

function checkForInitialValues () {
  parseToLatLng($("#id_start").val(), setStart, setStaticStart);
  parseToLatLng($("#id_end").val(), setEnd, setStaticEnd);
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

window.onload = init;
