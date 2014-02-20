var request = require ('request'),
	cheerio = require ('cheerio');

var addressCheck1 = "Waterloo, ON";
var addressCheck2 = "waterloo, ON";
var addressCheck3 = "Cambridge, ON";
var addressCheck4 = "cambridge, ON";
var addressCheck5 = "Kitchener, ON";
var addressCheck6 = "kitchener, ON";

locations = [];
var pages = 0;
var maxNumberPages = 29;


while (pages<maxNumberPages)
{
	var url = 'https://listings.och.uwaterloo.ca/Listings/Search/Results?page='+pages;
	request (url, function (err, resp, body){
		
		if (!err & resp.statusCode==200){

			var $ = cheerio.load(body);

			$('div#Rentals tr td span a').each(function(){

				if (this.text().indexOf(addressCheck1)!= -1 || this.text().indexOf(addressCheck2)!= -1 || this.text().indexOf(addressCheck3)!= -1 || this.text().indexOf(addressCheck4)!= -1 || this.text().indexOf(addressCheck5)!= -1 || this.text().indexOf(addressCheck6)!= -1 )
				{
					locations.push(this.text().trim());
				}

			});			
		}
	});

	console.log(locations);
	console.log(locations.length);

	pages++;
}


var map;
function initialize() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(43.472285, -80.544858);
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);