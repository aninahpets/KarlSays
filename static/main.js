console.log('JS loaded');

function initMap(restaurantLat, restaurantLng, activityLat, activityLng) {
        var activityLocation = {lat: activityLat, lng: activityLng};
        var restaurantLocation = {lat: restaurantLat, lng: restaurantLng};

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: activityLocation
        });

        var activityMarker = new google.maps.Marker({
          position: activityLocation,
          map: map,
        });

        var restaurantMarker = new google.maps.Marker({
          position: restaurantLocation,
          map: map,
        });
      }

// Event listener and handler for outing_type div click]

// Event listener and handler for outing_type div click
function setOutingType(evt) {
	// Sets outingType to be the data value of the div clicked
	var outingType = $(this).data('data-outing-type');
	console.log('Outing type chosen: ', outingType);
}
$(.outing-type).click(setOutingType);

function submitForm(evt) {
  string = JSON.stringify(formInputs,['outing-type','neighborhood'])
}

// Loading Gif and logic of when to display (on clicks)


// Event listener and handler for Map object
