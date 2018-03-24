from flask import Flask, jsonify, render_template
import pymongo
import requests as req
import json
import pprint
from bson.json_util import dumps
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.pokemon
collection = db.pokemon

@app.route("/get_data/<zipcode>")
def return_json(zipcode):
	gkey = "AIzaSyDzyP9E2Cr-NujfGLny6dFxi_gE9QVBi24"
	target_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + zipcode + "&key=" + gkey
	response = req.get(target_url).json()
	longitude = response["results"][0]["geometry"]["location"]["lng"]
	latitude = response["results"][0]["geometry"]["location"]["lat"]

	#print(response["results"])
	collection_data = collection.find({"loc": {"$near": {"$geometry": {"type": "Point", "coordinates": [longitude, latitude] }}}})

	closestPokemon = []
	foundPokemon = []

	for sighting in collection_data:
		if sighting["pokemonId"] not in foundPokemon:
			foundPokemon.append(sighting["pokemonId"])
			closestPokemon.append(sighting)
			if len(foundPokemon) == 150:
				break

	closestPokemon1 = closestPokemon[0:20]
	closestPokemon2 = closestPokemon[19:40]
	closestPokemon3 = closestPokemon[39:60]
	closestPokemon4 = closestPokemon[59:80]
	closestPokemon5 = closestPokemon[79:100]
	closestPokemon6 = closestPokemon[99:120]
	closestPokemon7 = closestPokemon[119:140]
	closestPokemon8 = closestPokemon[139:143]

	#print(closestPokemon8)



	target_url1 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon1[0]["latitude"]) + "," + str(closestPokemon1[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon1[1]["latitude"]) + "," + str(closestPokemon1[1]["longitude"]) + "|" +
				  str(closestPokemon1[2]["latitude"]) + "," + str(closestPokemon1[2]["longitude"]) + "|" +
				  str(closestPokemon1[3]["latitude"]) + "," + str(closestPokemon1[3]["longitude"]) + "|" +
				  str(closestPokemon1[4]["latitude"]) + "," + str(closestPokemon1[4]["longitude"]) + "|" +
				  str(closestPokemon1[5]["latitude"]) + "," + str(closestPokemon1[5]["longitude"]) + "|" +
				  str(closestPokemon1[6]["latitude"]) + "," + str(closestPokemon1[6]["longitude"]) + "|" +
				  str(closestPokemon1[7]["latitude"]) + "," + str(closestPokemon1[7]["longitude"]) + "|" +
				  str(closestPokemon1[8]["latitude"]) + "," + str(closestPokemon1[8]["longitude"]) + "|" +
				  str(closestPokemon1[9]["latitude"]) + "," + str(closestPokemon1[9]["longitude"]) + "|" +
				  str(closestPokemon1[10]["latitude"]) + "," + str(closestPokemon1[10]["longitude"]) + "|" +
				  str(closestPokemon1[11]["latitude"]) + "," + str(closestPokemon1[11]["longitude"]) + "|" +
				  str(closestPokemon1[12]["latitude"]) + "," + str(closestPokemon1[12]["longitude"]) + "|" +
				  str(closestPokemon1[13]["latitude"]) + "," + str(closestPokemon1[13]["longitude"]) + "|" +
				  str(closestPokemon1[14]["latitude"]) + "," + str(closestPokemon1[14]["longitude"]) + "|" +
				  str(closestPokemon1[15]["latitude"]) + "," + str(closestPokemon1[15]["longitude"]) + "|" +
				  str(closestPokemon1[16]["latitude"]) + "," + str(closestPokemon1[16]["longitude"]) + "|" +
				  str(closestPokemon1[17]["latitude"]) + "," + str(closestPokemon1[17]["longitude"]) + "|" + 
				  str(closestPokemon1[18]["latitude"]) + "," + str(closestPokemon1[18]["longitude"]) + "|" + 
				  "&destination=" + str(closestPokemon1[19]["latitude"]) + "," + str(closestPokemon1[19]["longitude"]) + "&key=" + gkey)

	target_url2 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon2[0]["latitude"]) + "," + str(closestPokemon2[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon2[1]["latitude"]) + "," + str(closestPokemon2[1]["longitude"]) + "|" +
				  str(closestPokemon2[2]["latitude"]) + "," + str(closestPokemon2[2]["longitude"]) + "|" +
				  str(closestPokemon2[3]["latitude"]) + "," + str(closestPokemon2[3]["longitude"]) + "|" +
				  str(closestPokemon2[4]["latitude"]) + "," + str(closestPokemon2[4]["longitude"]) + "|" +
				  str(closestPokemon2[5]["latitude"]) + "," + str(closestPokemon2[5]["longitude"]) + "|" +
				  str(closestPokemon2[6]["latitude"]) + "," + str(closestPokemon2[6]["longitude"]) + "|" +
				  str(closestPokemon2[7]["latitude"]) + "," + str(closestPokemon2[7]["longitude"]) + "|" +
				  str(closestPokemon2[8]["latitude"]) + "," + str(closestPokemon2[8]["longitude"]) + "|" +
				  str(closestPokemon2[9]["latitude"]) + "," + str(closestPokemon2[9]["longitude"]) + "|" +
				  str(closestPokemon2[10]["latitude"]) + "," + str(closestPokemon2[10]["longitude"]) + "|" +
				  str(closestPokemon2[11]["latitude"]) + "," + str(closestPokemon2[11]["longitude"]) + "|" +
				  str(closestPokemon2[12]["latitude"]) + "," + str(closestPokemon2[12]["longitude"]) + "|" +
				  str(closestPokemon2[13]["latitude"]) + "," + str(closestPokemon2[13]["longitude"]) + "|" +
				  str(closestPokemon2[14]["latitude"]) + "," + str(closestPokemon2[14]["longitude"]) + "|" +
				  str(closestPokemon2[15]["latitude"]) + "," + str(closestPokemon2[15]["longitude"]) + "|" +
				  str(closestPokemon2[16]["latitude"]) + "," + str(closestPokemon2[16]["longitude"]) + "|" +
				  str(closestPokemon2[17]["latitude"]) + "," + str(closestPokemon2[17]["longitude"]) + "|" + 
				  str(closestPokemon2[18]["latitude"]) + "," + str(closestPokemon2[18]["longitude"]) + "|" + 
				  "&destination=" + str(closestPokemon2[19]["latitude"]) + "," + str(closestPokemon2[19]["longitude"]) + "&key=" + gkey)

	target_url3 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon3[0]["latitude"]) + "," + str(closestPokemon3[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon3[1]["latitude"]) + "," + str(closestPokemon3[1]["longitude"]) + "|" +
				  str(closestPokemon3[2]["latitude"]) + "," + str(closestPokemon3[2]["longitude"]) + "|" +
				  str(closestPokemon3[3]["latitude"]) + "," + str(closestPokemon3[3]["longitude"]) + "|" +
				  str(closestPokemon3[4]["latitude"]) + "," + str(closestPokemon3[4]["longitude"]) + "|" +
				  str(closestPokemon3[5]["latitude"]) + "," + str(closestPokemon3[5]["longitude"]) + "|" +
				  str(closestPokemon3[6]["latitude"]) + "," + str(closestPokemon3[6]["longitude"]) + "|" +
				  str(closestPokemon3[7]["latitude"]) + "," + str(closestPokemon3[7]["longitude"]) + "|" +
				  str(closestPokemon3[8]["latitude"]) + "," + str(closestPokemon3[8]["longitude"]) + "|" +
				  str(closestPokemon3[9]["latitude"]) + "," + str(closestPokemon3[9]["longitude"]) + "|" +
				  str(closestPokemon3[10]["latitude"]) + "," + str(closestPokemon3[10]["longitude"]) + "|" +
				  str(closestPokemon3[11]["latitude"]) + "," + str(closestPokemon3[11]["longitude"]) + "|" +
				  str(closestPokemon3[12]["latitude"]) + "," + str(closestPokemon3[12]["longitude"]) + "|" +
				  str(closestPokemon3[13]["latitude"]) + "," + str(closestPokemon3[13]["longitude"]) + "|" +
				  str(closestPokemon3[14]["latitude"]) + "," + str(closestPokemon3[14]["longitude"]) + "|" +
				  str(closestPokemon3[15]["latitude"]) + "," + str(closestPokemon3[15]["longitude"]) + "|" +
				  str(closestPokemon3[16]["latitude"]) + "," + str(closestPokemon3[16]["longitude"]) + "|" +
				  str(closestPokemon3[17]["latitude"]) + "," + str(closestPokemon3[17]["longitude"]) + "|" + 
				  str(closestPokemon3[18]["latitude"]) + "," + str(closestPokemon3[18]["longitude"]) + "|" + 
				  "&destination=" + str(closestPokemon3[19]["latitude"]) + "," + str(closestPokemon3[19]["longitude"]) + "&key=" + gkey)

	target_url4 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon4[0]["latitude"]) + "," + str(closestPokemon4[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon4[1]["latitude"]) + "," + str(closestPokemon4[1]["longitude"]) + "|" +
				  str(closestPokemon4[2]["latitude"]) + "," + str(closestPokemon4[2]["longitude"]) + "|" +
				  str(closestPokemon4[3]["latitude"]) + "," + str(closestPokemon4[3]["longitude"]) + "|" +
				  str(closestPokemon4[4]["latitude"]) + "," + str(closestPokemon4[4]["longitude"]) + "|" +
				  str(closestPokemon4[5]["latitude"]) + "," + str(closestPokemon4[5]["longitude"]) + "|" +
				  str(closestPokemon4[6]["latitude"]) + "," + str(closestPokemon4[6]["longitude"]) + "|" +
				  str(closestPokemon4[7]["latitude"]) + "," + str(closestPokemon4[7]["longitude"]) + "|" +
				  str(closestPokemon4[8]["latitude"]) + "," + str(closestPokemon4[8]["longitude"]) + "|" +
				  str(closestPokemon4[9]["latitude"]) + "," + str(closestPokemon4[9]["longitude"]) + "|" +
				  str(closestPokemon4[10]["latitude"]) + "," + str(closestPokemon4[10]["longitude"]) + "|" +
				  str(closestPokemon4[11]["latitude"]) + "," + str(closestPokemon4[11]["longitude"]) + "|" +
				  str(closestPokemon4[12]["latitude"]) + "," + str(closestPokemon4[12]["longitude"]) + "|" +
				  str(closestPokemon4[13]["latitude"]) + "," + str(closestPokemon4[13]["longitude"]) + "|" +
				  str(closestPokemon4[14]["latitude"]) + "," + str(closestPokemon4[14]["longitude"]) + "|" +
				  str(closestPokemon4[15]["latitude"]) + "," + str(closestPokemon4[15]["longitude"]) + "|" +
				  str(closestPokemon4[16]["latitude"]) + "," + str(closestPokemon4[16]["longitude"]) + "|" +
				  str(closestPokemon4[17]["latitude"]) + "," + str(closestPokemon4[17]["longitude"]) + "|" + 
				  str(closestPokemon4[18]["latitude"]) + "," + str(closestPokemon4[18]["longitude"]) + "|" + 
				  "&destination=" + str(closestPokemon4[19]["latitude"]) + "," + str(closestPokemon4[19]["longitude"]) + "&key=" + gkey)

	target_url5 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon5[0]["latitude"]) + "," + str(closestPokemon5[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon5[1]["latitude"]) + "," + str(closestPokemon5[1]["longitude"]) + "|" +
				  str(closestPokemon5[2]["latitude"]) + "," + str(closestPokemon5[2]["longitude"]) + "|" +
				  str(closestPokemon5[3]["latitude"]) + "," + str(closestPokemon5[3]["longitude"]) + "|" +
				  str(closestPokemon5[4]["latitude"]) + "," + str(closestPokemon5[4]["longitude"]) + "|" +
				  str(closestPokemon5[5]["latitude"]) + "," + str(closestPokemon5[5]["longitude"]) + "|" +
				  str(closestPokemon5[6]["latitude"]) + "," + str(closestPokemon5[6]["longitude"]) + "|" +
				  str(closestPokemon5[7]["latitude"]) + "," + str(closestPokemon5[7]["longitude"]) + "|" +
				  str(closestPokemon5[8]["latitude"]) + "," + str(closestPokemon5[8]["longitude"]) + "|" +
				  str(closestPokemon5[9]["latitude"]) + "," + str(closestPokemon5[9]["longitude"]) + "|" +
				  str(closestPokemon5[10]["latitude"]) + "," + str(closestPokemon5[10]["longitude"]) + "|" +
				  str(closestPokemon5[11]["latitude"]) + "," + str(closestPokemon5[11]["longitude"]) + "|" +
				  str(closestPokemon5[12]["latitude"]) + "," + str(closestPokemon5[12]["longitude"]) + "|" +
				  str(closestPokemon5[13]["latitude"]) + "," + str(closestPokemon5[13]["longitude"]) + "|" +
				  str(closestPokemon5[14]["latitude"]) + "," + str(closestPokemon5[14]["longitude"]) + "|" +
				  str(closestPokemon5[15]["latitude"]) + "," + str(closestPokemon5[15]["longitude"]) + "|" +
				  str(closestPokemon5[16]["latitude"]) + "," + str(closestPokemon5[16]["longitude"]) + "|" +
				  str(closestPokemon5[17]["latitude"]) + "," + str(closestPokemon5[17]["longitude"]) + "|" + 
				  str(closestPokemon5[18]["latitude"]) + "," + str(closestPokemon5[18]["longitude"]) + "|" + 
				  "&destination=" + str(closestPokemon5[19]["latitude"]) + "," + str(closestPokemon5[19]["longitude"]) + "&key=" + gkey)

	target_url6 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon6[0]["latitude"]) + "," + str(closestPokemon6[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon6[1]["latitude"]) + "," + str(closestPokemon6[1]["longitude"]) + "|" +
				  str(closestPokemon6[2]["latitude"]) + "," + str(closestPokemon6[2]["longitude"]) + "|" +
				  str(closestPokemon6[3]["latitude"]) + "," + str(closestPokemon6[3]["longitude"]) + "|" +
				  str(closestPokemon6[4]["latitude"]) + "," + str(closestPokemon6[4]["longitude"]) + "|" +
				  str(closestPokemon6[5]["latitude"]) + "," + str(closestPokemon6[5]["longitude"]) + "|" +
				  str(closestPokemon6[6]["latitude"]) + "," + str(closestPokemon6[6]["longitude"]) + "|" +
				  str(closestPokemon6[7]["latitude"]) + "," + str(closestPokemon6[7]["longitude"]) + "|" +
				  str(closestPokemon6[8]["latitude"]) + "," + str(closestPokemon6[8]["longitude"]) + "|" +
				  str(closestPokemon6[9]["latitude"]) + "," + str(closestPokemon6[9]["longitude"]) + "|" +
				  str(closestPokemon6[10]["latitude"]) + "," + str(closestPokemon6[10]["longitude"]) + "|" +
				  str(closestPokemon6[11]["latitude"]) + "," + str(closestPokemon6[11]["longitude"]) + "|" +
				  str(closestPokemon6[12]["latitude"]) + "," + str(closestPokemon6[12]["longitude"]) + "|" +
				  str(closestPokemon6[13]["latitude"]) + "," + str(closestPokemon6[13]["longitude"]) + "|" +
				  str(closestPokemon6[14]["latitude"]) + "," + str(closestPokemon6[14]["longitude"]) + "|" +
				  str(closestPokemon6[15]["latitude"]) + "," + str(closestPokemon6[15]["longitude"]) + "|" +
				  str(closestPokemon6[16]["latitude"]) + "," + str(closestPokemon6[16]["longitude"]) + "|" +
				  str(closestPokemon6[17]["latitude"]) + "," + str(closestPokemon6[17]["longitude"]) + "|" + 
				  str(closestPokemon6[18]["latitude"]) + "," + str(closestPokemon6[18]["longitude"]) + "|" + 
				  "&destination=" + str(closestPokemon6[19]["latitude"]) + "," + str(closestPokemon6[19]["longitude"]) + "&key=" + gkey)

	target_url7 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon7[0]["latitude"]) + "," + str(closestPokemon7[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon7[1]["latitude"]) + "," + str(closestPokemon7[1]["longitude"]) + "|" +
				  str(closestPokemon7[2]["latitude"]) + "," + str(closestPokemon7[2]["longitude"]) + "|" +
				  str(closestPokemon7[3]["latitude"]) + "," + str(closestPokemon7[3]["longitude"]) + "|" +
				  str(closestPokemon7[4]["latitude"]) + "," + str(closestPokemon7[4]["longitude"]) + "|" +
				  str(closestPokemon7[5]["latitude"]) + "," + str(closestPokemon7[5]["longitude"]) + "|" +
				  str(closestPokemon7[6]["latitude"]) + "," + str(closestPokemon7[6]["longitude"]) + "|" +
				  str(closestPokemon7[7]["latitude"]) + "," + str(closestPokemon7[7]["longitude"]) + "|" +
				  str(closestPokemon7[8]["latitude"]) + "," + str(closestPokemon7[8]["longitude"]) + "|" +
				  str(closestPokemon7[9]["latitude"]) + "," + str(closestPokemon7[9]["longitude"]) + "|" +
				  str(closestPokemon7[10]["latitude"]) + "," + str(closestPokemon7[10]["longitude"]) + "|" +
				  str(closestPokemon7[11]["latitude"]) + "," + str(closestPokemon7[11]["longitude"]) + "|" +
				  str(closestPokemon7[12]["latitude"]) + "," + str(closestPokemon7[12]["longitude"]) + "|" +
				  str(closestPokemon7[13]["latitude"]) + "," + str(closestPokemon7[13]["longitude"]) + "|" +
				  str(closestPokemon7[14]["latitude"]) + "," + str(closestPokemon7[14]["longitude"]) + "|" +
				  str(closestPokemon7[15]["latitude"]) + "," + str(closestPokemon7[15]["longitude"]) + "|" +
				  str(closestPokemon7[16]["latitude"]) + "," + str(closestPokemon7[16]["longitude"]) + "|" +
				  str(closestPokemon7[17]["latitude"]) + "," + str(closestPokemon7[17]["longitude"]) + "|" + 
				  str(closestPokemon7[18]["latitude"]) + "," + str(closestPokemon7[18]["longitude"]) + "|" + 
				  "&destination=" + str(closestPokemon7[19]["latitude"]) + "," + str(closestPokemon7[19]["longitude"]) + "&key=" + gkey)

	target_url8 = ("https://maps.googleapis.com/maps/api/directions/json?origin=" + str(closestPokemon8[0]["latitude"]) + "," + str(closestPokemon8[0]["longitude"]) + "&waypoints=optimize:true|" + 
				  str(closestPokemon8[1]["latitude"]) + "," + str(closestPokemon8[1]["longitude"]) + "|" +
				  str(closestPokemon8[2]["latitude"]) + "," + str(closestPokemon8[2]["longitude"]) + "|" +
				  "&destination=" + str(closestPokemon8[3]["latitude"]) + "," + str(closestPokemon8[3]["longitude"]) + "&key=" + gkey)

	print(target_url8)

	response1 = req.get(target_url1).json()
	response2 = req.get(target_url2).json()
	response3 = req.get(target_url3).json()
	response4 = req.get(target_url4).json()
	response5 = req.get(target_url5).json()
	response6 = req.get(target_url6).json()
	response7 = req.get(target_url7).json()
	response8 = req.get(target_url8).json()

	legs = []
	legs.append(response1["routes"][0]["legs"])
	legs.append(response2["routes"][0]["legs"])
	legs.append(response3["routes"][0]["legs"])
	legs.append(response4["routes"][0]["legs"])
	legs.append(response5["routes"][0]["legs"])
	if response6["status"] != "ZERO_RESULTS":
		legs.append(response6["routes"][0]["legs"])
	if response7["status"] != "ZERO_RESULTS":
		legs.append(response7["routes"][0]["legs"])
	if response8["status"] != "ZERO_RESULTS":
		legs.append(response8["routes"][0]["legs"])

	#print(response8)
	
	return jsonify(legs)

if __name__ == "__main__":
    app.run(debug=True)