console.log('JS loaded');


// Event listener and handler for outing_type div click
function setOutingType(evt) {
	// Sets outingType to be the data value of the div clicked
	var outingType = $(this).data('data-outing-type');
	console.log('Outing type chosen: ', outingType);
}
$(.outing-type).click(setOutingType);



// Event handler for setting Neighborhood
function setNeighborhood(evt) {
	// Get value of neighborhood
	var neighborhood = $('#neighborhood-button')
	('data-neighborhood-type').value();
}
$('#neighborhood-button').click(setNeighborhood);


// Loading Gif and logic of when to display (on clicks)


// Event listener and handler for Map object
