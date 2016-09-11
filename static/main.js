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

// Event listener and handler for neighborhood dropdown

// Loading Gif and logic of when to display (on clicks)

// Event listener and handler for Map object
