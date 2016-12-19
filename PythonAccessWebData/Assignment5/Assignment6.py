# A Python that will prompt for a location, contact a web service and retrieve
# JSON for the web service and parse that data, and retrieve the first place_id
# from the JSON. A place ID is a textual identifier that uniquely identifies a
# place as within Google Maps.

# Sample location: "South Federal University"
# Actual location: "University of Cambridge"

import urllib
import json

serviceUrl = "http://python-data.dr-chuck.net/geojson?"
keepSearching = True

while keepSearching:
    address = raw_input("Please enter a location: ")
    url = serviceUrl + urllib.urlencode({'sensor': 'false', 'address': address})

    print "Retrieving:", url
    urlHandler = urllib.urlopen(url)

    data = urlHandler.read()
    print "Retrieved", len(data), "characters"

    try:
        jsonString = json.loads(str(data))

    except:
        jsonString = None

    if 'status' not in jsonString or jsonString['status'] != 'OK':
        print "*** FAILURE TO RETRIEVE ***"
        print data

    place_id = jsonString['results'][0]['place_id']
    print place_id

    searchAgain = raw_input("Would you like to continue? (Y or N): ")

    if searchAgain.lower() == 'n' or searchAgain.lower() == 'no':
        keepSearching = False
