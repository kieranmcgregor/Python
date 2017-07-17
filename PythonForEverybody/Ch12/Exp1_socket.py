import socket
import time

PORT = 80
HOST = input("Please enter the request URL:\n")
REQ_FILE = input("Please enter a request file path:\n")

if (len(HOST) < 1):
    print("Using default host, data.pr4e.org")
    HOST = 'data.pr4e.org'

if (len(REQ_FILE) < 1):
    print("Using default host, data.pr4e.org")
    REQ_FILE = '/cover.jpg'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
command = 'GET ' + REQ_FILE + ' HTTP/1.0\r\nHost: ' + HOST + '\r\n\r\n'
mysock.sendall(command.encode())

count = 0
picture = b""
busy = True

while busy:
    data = mysock.recv(5120)

    if (len(data) < 1):
        busy = False
    else:
        time.sleep(0.25)
        count = count + len(data)
        print(len(data), count)
        picture = picture + data

mysock.close

header_end = "\r\n\r\n"
pos = picture.find(header_end.encode())
print('Header length', pos)
print(picture[:pos].decode())

picture_data_start = pos + len(header_end)
picture = picture[(picture_data_start):]

if(len(picture) > 0):
    save_name = input("Please enter a file save name:\n")

    if(len(save_name) < 1):
        print ("Using default file save name, stuff.jpg")
        save_name = "stuff.jpg"

    save_path = "../Files/" + save_name
    fhand = open(save_path, "wb")
    fhand.write(picture)
    fhand.close()
else:
    print("ERROR: No data found check that file path is valid.")
