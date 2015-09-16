import requests
import json
from sys import exit
from operator import itemgetter

#Ask user for pub ID
inputURL = input("Please paste the Hubski URL here: ")

#Check if it's a full URL. If so, slice it to only have the pub ID left.
if inputURL.startswith("https://hubski.com/pub?id="):
    pubID = inputURL[26:]
else:
    print('Incorrect URL. Needs to be in the format "https://hubski.com/pub?id=[number]"')
    input("Press Enter to exit...")
    raise SystemExit

#Check if that ID exists in the publications list. If it doesn't, stop the script. 
pubIDlistURL = requests.get("http://api.hubski.com/publications")
pubIDlist = pubIDlistURL.text
if pubID in pubIDlist:
    pass
else:
    print('Post/comment does not exist or is not accessible')
    input("Press Enter to exit...")
    raise SystemExit

#Concenate to create new URL
url = "http://api.hubski.com/publication/" + pubID
print(url)

#Open url, get data into a json  
http = requests.get(url)
data = http.json()

#Sort votes from first to last. 
votes = data['votes']
sortedVotes = sorted(votes, key=itemgetter('id'), reverse=False)

#Print the names and add a number in front as a count
count = 0
print ('Pub ID: ' + pubID + '\nTitle: ' + str(data["title"]) + \
'\nList of votes, sorted from first voter to last:')

for user in sortedVotes:
    count += 1
    if user['up'] == True:
        vote = 'up' 
    else: 
        vote = 'down'
    print(str(count) + ': ' + user['user'] + ' voted ' + vote)

input("Press Enter to exit...")

#__________________________________________________
#Legacy code: Pretty Json printer
#print(json.dumps(data, indent=4, sort_keys=True))