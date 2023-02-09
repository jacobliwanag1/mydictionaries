'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''



import json

infile = open('eq_data.json','r')

earthquakes = json.load(infile)

conference_schools = [372,108,107,130]

#print(earthquakes)
print()
print('Number of earthquakes:')
print(earthquakes["metadata"]["count"])




eg_dict= {}

print(eg_dict)

for i in range(6274):
   if(earthquakes["features"][i]["properties"]["mag"])>6:
      
      location= earthquakes["features"][i]["properties"]["place"]
      eg_dict[i]=location
      magnitude=earthquakes["features"][i]["properties"]["mag"]
      eg_dict[i]=magnitude
      longitude=earthquakes["features"][i]["geometry"]["coordinates"][0]
      eg_dict[i]=longitude
      latitude=earthquakes["features"][i]["geometry"]["coordinates"][1]
      eg_dict[i]=latitude


print(eg_dict)
print()

for i in range(6274):
   if(earthquakes["features"][i]["properties"]["mag"])>6:
      
      location= earthquakes["features"][i]["properties"]["place"]
      print('Location:',location)
      magnitude=earthquakes["features"][i]["properties"]["mag"]
      print('Magnitude:',magnitude)
      longitude=earthquakes["features"][i]["geometry"]["coordinates"][0]
      print('Longitude:',longitude)
      latitude=earthquakes["features"][i]["geometry"]["coordinates"][1]
      print('Latitude:',latitude)

      print()
      print()