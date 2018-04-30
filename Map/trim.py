#Python CSV Trimming script

import csv
import json

file = open('locations.csv', 'w')

with open("yellow_tripdata_2016-02.csv") as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		file.write('{'+ 'lat: '+ row['pickup_latitude'] + ', ' + 'lng: ' + row['pickup_longitude'] + '}' + ',' + '\n')



file.close()



