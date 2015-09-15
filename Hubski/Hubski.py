import requests
import json
from sys import exit
from operator import itemgetter

#Ask user for pub ID. Slice to get the Pub ID
inputURL = input("Please paste the Hubski URL here: ")
pubID = inputURL[26:]

#Check if that ID exists in the publications list. If it doesn't, stop the script. 
pubIDlistURL = requests.get("http://api.hubski.com/publications")
pubIDlist = pubIDlistURL.text
if pubID in pubIDlist:
    pass
else:
    print('Pub ID does not exist or is not accessible')
    raise SystemExit

#Concenate to create new URL
url = "http://api.hubski.com/publication/" + pubID
print(url)

#Open url, get data into a json  
http = requests.get(url)
data = http.json()

#Sort votes from first to last. 
votes = data['votes']
sortedVotes = sorted(votes, key=itemgetter('num'), reverse=False)

#Print the names and add a number in front as a count
count = 0
print ('List of votes, sorted from first voter to last:')
for user in sortedVotes:
    count += 1
    print(str(count) + ': ' + user['user'])

#__________________________________________________
#Legacy code
#print(json.dumps(data, indent=4, sort_keys=True))