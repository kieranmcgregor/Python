import urllib.request, urllib.parse, urllib.error
import time
import re

def doc_downloader(URL):
    downloading = True
    protocol = "http"
    doc = ""

    if (protocol not in URL):
        url_parts = urllib.parse.urlparse(URL)
        URL = ('http://' + url_parts[1] + url_parts[2] + url_parts[3] + url_parts[4] +url_parts[5])

    fhand = urllib.request.urlopen(URL)

    for line in fhand:
        doc += line.decode()

    size = len(doc)

    return (doc, size)

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
    LIMIT = 3000

    count = 0
    doc = b""

    print("**-- This program will save all downloads in a .txt format --**")

    while downloading:
        URL = input("Please enter a URL for the file you wish to download:\n")

        if (URL == 'q'):
            downloading = False
        else:
            try:
                doc, size = doc_downloader(URL)
                downloading = False
            except:
                print ("Invalid URL, please check and renter URL")

    if (len(doc) > 0):
        doc_saver(doc)
        print(doc[:LIMIT+1] + "\n" + str(size))

main()
