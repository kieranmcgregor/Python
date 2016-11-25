#use urllib to read the HTML from the data files, extract the href= values from
#the anchor tags, scan for a tag that is in a particular position relative to
#the first name in the list, follow that link and repeat the process a number
#of times and report the last name found

#Sample problem: Start at: http://python-data.dr-chuck.net/known_by_Fikret.html
#Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Presley.html

import urllib
from BeautifulSoup import *

def readPrintUrlContent(url):
    print "Retreiving:", url
    return urllib.urlopen(url).read()

url = raw_input("Enter a URL - ")
position = raw_input("Enter an integer position - ")
times = raw_input("Enter an integer repeat value - ")

try:
    offsetPosition = int(position) - 1
    times = int(times)

except:
    print ("Invalid position or times input, using default: 3, 4")
    offsetPosition = 3 - 1
    times = 4

while(times > 0):
    try:
        html = readPrintUrlContent(url)

    except:
        print("Unrecognizable URL, using default URL: http://python-data.dr-chuck.net/known_by_Fikret.html")
        url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
        html = readPrintUrlContent(url)

    soup = BeautifulSoup(html)

    tags = soup('a')

    for index, tag in enumerate(tags):
        if(index == (offsetPosition)):
            url = tag.get("href", None)

    times -= 1

print "Retreiving:", url
