import sqlite3
import re

connection = sqlite3.connect('emaildb.sqlite')
cursor = connection.cursor()

cursor.execute('''
DROP TABLE IF EXISTS Counts''')

cursor.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fileName = raw_input('Enter file name: ')

try:
    fileHandler = open(fileName)

except:
    print("file not found, using default: mbox.txt")
    fileName = 'mbox.txt'
    fileHandler = open(fileName)

for line in fileHandler:
    if line.startswith('From: '):
        pieces = line.split()
        email = pieces[1]
        atIndex = email.find('@')
        org = email[(atIndex + 1):]
        print org
        cursor.execute('SELECT count FROM counts WHERE org = ?', (org, ))
        row = cursor.fetchone()

        if row is None:
            cursor.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org, ))
        else:
            cursor.execute('UPDATE Counts SET count=count+1 WHERE org=?', (org, ))


connection.commit()

sqlString = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cursor.execute(sqlString):
    print str(row[0]), row[1]

cursor.close()
