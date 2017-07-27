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
