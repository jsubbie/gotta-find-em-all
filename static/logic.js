// Mapbox API

var mapbox = "https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ.T6YbdDixkOBWH_k9GbS8JQ";

// Creating map object
var myMap = L.map("map", {
  center: [40.7, -73.95],
  zoom: 3
});

// Adding tile layer to the map
L.tileLayer(mapbox).addTo(myMap);

// Building API query URL

//var baseURL = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?";
//var date = "$where=created_date between'2016-01-10T12:00:00' and '2017-01-01T14:00:00'";
//var complaint = "&complaint_type=Rodent";
//var limit = "&$limit=10000";
// Assembling API query URL
/*
var baseURL = {
        "Abilities": "['Insomnia', 'Forewarn', 'Inner Focus']",
        "AppearedDay": "2",
        "AppearedDayOfWeek": "Tuesday",
        "AppearedLocalTime": "9/2/16 9:50:06 PM",
        "AppearedMonth": "8",
        "AppearedTimeOfDay": "night",
        "AppearedYear": "2016",
        "City": "Prague",
        "Class": "96",
        "Classfication": "Hypnosis Pokémon",
        "CloseToWater": "False",
        "Continent": "Europe",
        "Generation": "1",
        "IsLegendary": "0",
        "JapaneseName": "Sleepeスリープ",
        "Latitude": "50.144272",
        "Longitude": "14.101178",
        "Name": "Drowzee",
        "NumberofRecords": "1",
        "PercentageMale": "50",
        "PokedexNumber": "96",
        "PokemonId": "96",
        "SpAttack": "43",
        "SpDefense": "90",
        "Speed": "42",
        "TerrainType": "12",
        "Type1": "psychic",
        "Type2": "",
        "Weather": "Clear",
        "WeightKg": "32.4",
        "_Id": "MTMzNzM3NzQ1MTM4MTcwMTE0Njk="
    };
*/

  var jsonURL = "/static/PokemonData.json";

  d3.json(jsonURL, function(error, response) {
  console.log("test");
  console.log(error);
  console.log(response);


  var $PokemonSelectBtn = document.querySelector(".panel .btn.btn-primary");

// Add click event listeners to the buttons, call the functions passed in
  $PokemonSelectBtn.addEventListener("click", handlePokemonButtonClick);
 
  var markers = L.markerClusterGroup();



  function handlePokemonButtonClick() {


          markers.clearLayers();

           var pokemonSelected  =  document.getElementById("PokemonName").value;

           console.log("onclick"+pokemonSelected);

          // Creating a new marker cluster group

            //myMap.removeLayer(markers);


            //markers.clearLayers();

            //console.log("remove marker layer");

          // Loop through our data...
            for (var i = 0; i < response.length; i++) {
            // set the data location property to a variable
              var Lat = response[i].Latitude;
              var Lon = response[i].Longitude;

            // If the data has a location property...
              if (Lat) {


            var pokemonIcon = L.icon({
                iconUrl:  response[i].ImageURL,
                iconSize:     [100, 100], // size of the icon
                iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
                popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
            });

            if (pokemonSelected == "All"  || pokemonSelected == response[i].Name) {

                  if (response[i].ImageURL) { 
                    markers.addLayer(L.marker([Lat, Lon], {icon: pokemonIcon})
                    .bindPopup("Name : " + response[i].Name + " Type : " + response[i].Type2  + "<br>Weather : <br>" + response[i].Weather + pokemonIcon));
                  }

                  else {
                    markers.addLayer(L.marker([Lat, Lon])
                    .bindPopup("Name : " + response[i].Name + " Type : " + response[i].Type2  + "<br>Weather : <br>" + response[i].Weather));      
                  }

                   }
                 }
          }


            myMap.addLayer(markers);
        }

});

//Get reference to zipcode search button
var searchFieldZip = document.getElementById("zip");
var searchBtnZip = document.getElementById("searchzip"); 

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
searchBtnZip.addEventListener("click", handleSearchButton);

var polyLineMarkers = L.markerClusterGroup();

function handleSearchButton(user_input) {
console.log('search zip clicked');
var user_input = searchFieldZip.value;

var polyLineUrl = "/get_data/" + user_input;
console.log(user_input)


polyLineMarkers.clearLayers();

 d3.json(polyLineUrl, function(error, response) {
 console.log("pulled polyLineUrl");
 console.log(error);
 console.log(response);

if(response){
  for (i=0; i<response.length; i++){
   for (j=0; j<response[i].length; j++){
     for (k=0; k<response[i][j].steps.length; k++){
       console.log(response[i][j].steps[k].polyline.points);
       polyLineMarkers.addLayer(L.Polyline.fromEncoded(response[i][j].steps[k].polyline.points))
     }
   }
  }
  myMap.addLayer(polyLineMarkers);
}

});

};

