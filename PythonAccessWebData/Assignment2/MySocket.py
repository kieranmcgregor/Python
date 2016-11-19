#retrieve http://data.pr4e.org/intro-short.txt using the HTTP protocol in a way
#that you can examine the HTTP Response headers

import socket
import re

def socketConnector(website):
    mySocket.connect((website, 80))

def requestSender(webHost, webDoc):
    getRequest = 'GET http://' + webHost + '/' + webDoc + ' HTTP/1.0\n\n'
    mySocket.send(getRequest)

webHost = raw_input("Please enter a URL: ")
webDoc = raw_input ("Please enter a file for retrieval: ")

try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketConnector(webHost)
    requestSender(webHost, webDoc)

except:
    print ('Invalid URL or file using defaults: data.pr4e.org/intro-short.txt')
    webHost = 'data.pr4e.org'
    webDoc = 'intro-short.txt'
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketConnector(webHost)
    requestSender(webHost, webDoc)

dataTransfering = True

while dataTransfering:
    data = mySocket.recv(512)
    if ( len(data) < 1 ) :
        dataTransfering = False
    print data

mySocket.close()
