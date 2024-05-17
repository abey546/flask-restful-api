#used for testing purposes

import requests
import json

BASE = "http://127.0.0.1:5000/"
data = {"views": 100}
#data = [{"likes": 30000, "name": "hoe to make pancake", 'views': 100000},
        #{"likes": 6000, "name": "learn python", 'views': 133000},
        #{"likes": 10003, "name": "learn rest api", 'views': 200000}] # Your data in a dictionary
#Set Content-Type header to application/json
headers = {"Content-Type": "application/json"}

#for i in range(len(data)):
    #response = requests.put(BASE + "video/" + str(i), json=data[i], headers=headers)
    #print(response.json())

#response = requests.put(BASE + "video/1", json=data, headers=headers)

#response = requests.post(BASE + "video/1", {"likes": 10})
#print(response.json())

#input()

#response = requests.delete(BASE + "video/0")
#print(response)
#input()

response = requests.patch(BASE + "video/2", json=data, headers=headers)
print(response.json())
