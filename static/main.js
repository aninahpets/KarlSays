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

//   function setOutingType(evt) {
//       // Sets outingType to be the data value of the div clicked
//       var outingType = $(this).data('data-outing-type');
//       console.log('Outing type chosen: ', outingType);
//     }

//     $('.outing-type').click(setOutingType);

//     console.log($(this).data('data-neighborhood-type'));
//     console.log($(this).data('data-outing-type'));

//     function submitForm(evt) {
//       formInputs = {"neighborhood": $(this).data('data-neighborhood-type'),
//                    "outing_type": $(this).data('data-outing-type')
//                   };
//       var string = JSON.stringify(formInputs,['neighborhood','outing_type']);
//       console.log(string);


//      $.post("/adventure_submit.json",
//             formInputs,
//             displayAdventure);
//     };
// })();

funtion displayAdventure(){
  console.log("Got an Adventure");
  // GET YELP BUSINESS NAME, URL, COORDINATES
  var yelp_url = 'https://www.yelp.com/biz/park-tavern-san-francisco'
  var yelp_name = 'Park Tavern'
  var yelp_lat = '37.801091'
  var yelp_long = '-122.409095'
  // DATABASE QUERY RESULT NAME, URL, COORDINATES
  var park_name = 'South End Rowing/Dolphin Club'
  var park_lat = '37.80796044'
  var park_long = '-122.42126376'

  //AJAX SOME SHIT ON THE DIVS
  $('#food_info').html(yelp_name);
  $('#food_info').attr("href", yelp_url);
  $('#outing_info').html(park_name);
  $('#outing_info').attr("href", yelp_url);


  // RENDER MAP
  function initMap(yelp_lat, yelp_long, park_lat, park_long) {
          var activityLocation = {lat: park_lat, lng: park_long};
          var restaurantLocation = {lat: yelp_lat, lng: yelp_long};

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

}

$('#neighborhood-button').click(displayAdventure);


// Loading Gif and logic of when to display (on clicks)


