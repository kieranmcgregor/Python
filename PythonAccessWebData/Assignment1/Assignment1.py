#extract data from regex_sum_42.txt sample file and regex_sum_333838.txt
#for true tests

import re

numbersList = []

fileName = raw_input("What file would you like to open? ")

try:
    fileHandle = open(fileName)

except:
    print "file not found, opening sample file regex_sum_42.txt"
    fileHandle = open("regex_sum_42.txt")

for file in fileHandle:
    file = file.strip()
    numberString = re.findall('([0-9]+)', file)

    if len(numberString) != 1: continue
    number = float(numberString[0])
    numbersList.append(number)
        
print numbersList
