#a Python program that will prompt for a URL, read the XML data from that URL
#using urllib and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.

#Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_333840.xml (Sum ends with 77)

import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location: ")
runningSum = 0

try:
    print "Retrieving", url
    urlHandler = urllib.urlopen(url)


except:
    print "Invalid url, using default: http://python-data.dr-chuck.net/comments_42.xml"
    url = "http://python-data.dr-chuck.net/comments_42.xml"
    print "Retrieving", url
    urlHandler = urllib.urlopen(url)

data = urlHandler.read()
print "Retrieving", len(data), "characters"

tree = ET.fromstring(data)

results = tree.findall('comments/comment')
for item in results:
    commentCount = int(item.find('count').text)
    print 'Count:', commentCount
    runningSum += commentCount

print "Sum:", runningSum
