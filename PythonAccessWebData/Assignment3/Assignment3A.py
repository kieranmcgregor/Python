#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers
#in the file.

#We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.

#Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_333843.html (Sum ends with 83)

import urllib
from BeautifulSoup import *

runningTotal = 0

url = raw_input("Enter - ")

try:
    html = urllib.urlopen(url).read()

except:
    print ("Unrecognized URL, using default URL: http://python-data.dr-chuck.net/comments_42.html")
    html = urllib.urlopen("http://python-data.dr-chuck.net/comments_42.html").read()

soup = BeautifulSoup(html)

tags = soup('span')

for tag in tags:
    value = tag.contents[0]
    print value

    try:
        runningTotal += int(value)

    except:
        print ("Content value not an integer, skipping value")

print runningTotal
