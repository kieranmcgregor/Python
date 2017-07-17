import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
command = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(command)

busy = True

while busy:
    data = mysock.recv(512)
    if (len(data) < 1):
        busy = False
    else:
        print(data.decode())

mysock.close()
