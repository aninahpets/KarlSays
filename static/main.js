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

// Event listener and handler for outing_type div click
(function() {

  function setOutingType(evt) {
      // Sets outingType to be the data value of the div clicked
      var outingType = $(this).data('data-outing-type');
      console.log('Outing type chosen: ', outingType);
    }

    $(.outing-type).click(setOutingType);
    console.log($(this).data('data-neighborhood-type'));
    console.log($(this).data('data-outing-type'));
    function submitForm(evt) {
      formInputs = {"neighborhood": $(this).data('data-neighborhood-type'),
                   "outing_type": $(this).data('data-outing-type')
                  };
      var string = JSON.stringify(formInputs,['neighborhood','outing_type']);
      console.log(string);


     $.post("/adventure_submit.json",
            formInputs,
            displayAdventure);
    });
}();

funtion displayAdventure(result){
  console.log("Got an Adventure", result);

}

// Loading Gif and logic of when to display (on clicks)


