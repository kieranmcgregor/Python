import socket
import time
import re

def quit():
    no_quit = ""
    no_answer = True

    while no_answer:
        answer = input("Would you like to continue? (y/n) ")

        try:
            no_quit = answer[0].lower()
            no_answer = False
        except:
            print ("Invalid entry please enter 'y' for yes and 'n' for no.")
            continue

    if no_quit == 'y':
        return True
    elif no_quit != 'n':
        print ("Neither 'y' nor 'n' found, exiting program")

    return False

def fname_builder():
    fname = ""
    fpath = ""
    file_ext = '.txt'

    nameless = True

    while nameless:
        fname = input("""Please specify a file name for opening or saving of HTTP Standards
document or enter '.' for default file name "file.txt":\n""")

        if (len(fname) > 0):
            if(fname[0] == '.'):
                fname = 'file.txt'
            elif(file_ext not in fname):
                fname += '.'
                print ("Invalid file extension, adding .txt file extension...\n")
                fname = re.findall('^(.+?)[.]', fname)[0]
                fname += file_ext
                print(fname)

            nameless = False
        else:
            print("""Invalid entry, please specify a file name for opening or saving of
            HTTP Standards document.\n""")

    fpath = input("""\nPlease specify a file path if one exists or enter '.' for default
file path "../Files/", else press 'Enter' to save document in current directory:\n""")

    if(fpath == '.'):
        fpath = '../Files/'

    if(len(fpath) > 0 and fpath[-1] != '/' and fname[0] != '/'):
        fpath += '/'

    return (fpath + fname)

def doc_downloader(fname):
    PORT = 80
    HOST, PATH = url_requester()
    HEADER_END = '\r\n\r\n'

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, PORT))

    command = "GET " + PATH + " HTTP/1.0\r\nHost: " + HOST + HEADER_END
    mysock.sendall(command.encode())

    count = 0
    doc = b""

    busy = True

    while busy:
        data = mysock.recv(5120)

        if (len(data) < 1):
            busy = False
        else:
            time.sleep(0.25)
            count = count + len(data)
            print(len(data), count)
            doc = doc + data

    mysock.close()

    pos = doc.find(HEADER_END.encode())
    print ("Header length:", pos)
    print (doc[:pos].decode())

    doc_data_start = pos + len(HEADER_END)
    doc = doc[doc_data_start:]

    if(len(doc) > 0):
        save_name = fname
        fhand = open(save_name, "wb")
        fhand.write(doc)
        fhand.close()
    else:
        print("ERROR: No data found check that URL is valid.")

def url_requester():
    host = ""
    path = ""
    empty_url = True

    while empty_url:

        URL = input("Please enter a URL for download:\n")

        try:
            host = re.findall('^http.*://(\S+?)/', URL)[0]
        except:
            host = re.findall('^(\S+?)/', URL)[0]

        try:
            path = re.findall('^http.*://\S+?(/\S+)', URL)[0]
        except:
            path = re.findall('^\S+?(/\S+)', URL)[0]

        if (len(host) < 1 and len(path) < 1):
            print ("Invalid host and path in URL, ie. www.example.com/file.txt not found")
        elif (len(host) < 1):
            print ("Invalid host in URL, ie. www.example.com not found")
        elif (len(path) < 1):
            print ("Invalid path in URL, ie. www.example.com/file.txt not found")
        else:
            empty_url = False

    return (host, path)

def file_reader(fhand):
    quit_message = """**- At any break input [q] to quit reading. -**\n\n
Press 'Enter' to continue reading\n\n"""

    pause = input(quit_message)

    for line in fhand:
        line = line.strip()

        if (len(line) > 0):
            print(line)

            quit = input("")

            if (len(quit) > 0 and quit[0].lower() == 'q'):
                break
            elif (len(quit) > 0 and quit[0].lower() != 'q'):
                pause = input(quit_message)

def main():
    no_quit = True
    doc_empty = True

    while doc_empty and no_quit:
        fname = fname_builder()

        try:
            fhand = open(fname)
            print("Opening " + fname + "...\n\n")
            doc_empty = False
        except:
            try:
                save_name = fname
                fhand = open(save_name, "wb")
                fhand.close()

                try:
                    doc_downloader(fname)
                    fhand = open(fname)
                    doc_empty = False
                except:
                    print("Invalid URL, please retry entering URL.")
                    no_quit = quit()

            except:
                print("Invalid file path, please retry entering file path.")
                no_quit = quit()

    if(no_quit):
        file_reader(fhand)
        fhand.close()

main()
