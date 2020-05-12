import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'LV ActivePower (kW)':2647.506104, 'Wind Speed (m/s)':10.345970, 'Wind Direction (°)':190.715607,'Month' :   3.000000,'Day' : 2.000000,'Hour' : 11.000000,'Year' : 2018.000000})

print(r.json())
		
