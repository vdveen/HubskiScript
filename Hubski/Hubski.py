import requests
import json
import pprint

# 1) Open url, 2) Get data into a json 3) Show the pretty version  
http = requests.get("http://api.hubski.com/publication/266825")
data = http.json()
print(json.dumps(data, indent=4, sort_keys=True))

#print(http.headers['content-type']) in case i get more unicode errors


