# A Python program that will prompt for a URL, read the JSON data from that URL
# using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file.

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_333844.json (Sum ends with 35)
import urllib
import json

def settingDefaultURL(message):
    print message + ", using default URL: http://python-data.dr-chuck.net/comments_42.json"
    url = "http://python-data.dr-chuck.net/comments_42.json"
    return urllib.urlopen(url)

url = raw_input("Please enter JSON related URL: ")
runningSum = 0

try:
    print "Retrieving", url
    urlHandler = urllib.urlopen(url)

except:
    message = "Invalid URL"
    urlHandler = settingDefaultURL(message)

data = urlHandler.read()

try:
    parsedData = json.loads(data)

except:
    message = "JSON data not found"
    urlHandler = settingDefaultURL(message)
    data = urlHandler.read()
    parsedData = json.loads(data)

for person in parsedData['comments']:
    runningSum += person['count']

print runningSum
