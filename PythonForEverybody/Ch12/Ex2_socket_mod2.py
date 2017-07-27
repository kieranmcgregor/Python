import socket
import time
import re

def doc_downloader(HOST, PATH, HEADER_END):
    PORT = 80

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, PORT))

    command = "GET " + PATH + " HTTP/1.0\r\nHost: " + HOST + HEADER_END
    mysock.sendall(command.encode())

    count = 0
    doc = b""

    downloading = True

    while downloading:
        data = mysock.recv(5120)

        if(len(data) < 1):
            downloading = False

        time.sleep(0.25)
        count += len(data)
        print(len(data), count)
        doc += data

    mysock.close()

    return (doc, count)

def yorn(question):
    asking = True
    act = True

    while asking:
        answer = input(question + "\n(Please enter [y]es or [n]o): ")

        if (answer.lower()[0] == 'n'):
            act = False
        elif (answer.lower()[0] != 'y'):
            print ("Neither 'y' nor 'n' selected.")
            continue

        asking = False

    return act

def doc_saver(doc):
    file_ext = 'txt'
    question = 'Would you like to save the file?'
    saving = yorn(question)

    while saving:
        save_name = input("Please enter a file save name:\n")
        save_name_parts = save_name.split('.')
        save_name = save_name_parts[0]

        if (len(save_name_parts) > 1):
            for part in save_name_parts:
                if (part == file_ext):
                    save_name += '.' + part
                    break
                elif (part != save_name):
                    save_name += "_" + part
                    print("""Replacing period ('.') with underscore ('_'), file
save name now reads {}""".format(save_name))

        if (file_ext not in save_name):
            save_name += file_ext

        save_path = input("Please enter a file save path if there is one:\n")
        if (len(save_path) > 0 and save_path[-1] != '/'):
            save_path = save_path + '/'

        save_name = save_path + save_name

        try:
            fhand = open(save_name, 'wb')
            fhand.write(doc)
            fhand.close()
            saving = False
        except:
            print("Invalid file path or file name, please check file path and file name.")
            question = 'Would you like to save the file?'
            saving = yorn(question)

def main():
    downloading = True
    HOST = ""
    PATH = ""
    HEADER_END = '\r\n\r\n'
    LIMIT = 3000

    count = 0
    doc = b""

    print("**-- This program will save all downloads in a .txt format --**")

    while downloading:
        URL = input("Please enter a URL for the file you wish to download:\n")

        if (URL == 'q'):
            downloading = False

        else:
            url_parts = URL.split('/')

            for part in url_parts:
                if '.' in part and part != url_parts[-1]:
                    HOST = part
                elif (len(HOST) > 0):
                    PATH += '/' + part
            try:
                doc, count = doc_downloader(HOST, PATH, HEADER_END)
                downloading = False
            except:
                print ("Invalid URL, please check and renter URL")

    if (len(doc) > 0):
        pos = doc.find(HEADER_END.encode())
        print('Header length', pos)
        print(doc[:pos].decode())

        doc = doc[pos + len(HEADER_END):]
        doc_saver(doc)

        print(doc[:LIMIT + 1].decode() + "\n" + str(count))
main()
