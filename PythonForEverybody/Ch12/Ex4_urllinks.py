import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def yorn(question, act):
    asking = True

    while asking:
        answer = input(question + "\n(Please enter [y]es or [n]o): ")

        if (answer.lower()[0] == 'n'):
            act = not act
        elif (answer.lower()[0] != 'y'):
            print ("Neither [y]es nor [n]o selected.")
            continue

        asking = False

    return act

def main():
    PROTOCOL = 'http'
    html = b""
    url_empty = True
    live = True

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while (url_empty and live):
        url = input('Enter - ')

        if (PROTOCOL not in url):
            url_parts = urllib.parse.urlparse(url)
            url = 'http://' + url_parts[1] + url_parts[2] + url_parts[3] + url_parts[4] + url_parts[5]

        try:
            html = urllib.request.urlopen(url, context=ctx).read()
            url_empty = False
        except:
            print ("Invalid URL, please check and renter URL")
            live = yorn('Would you like to continue?', live)

    if (len(html) > 0):
        soup = BeautifulSoup(html, 'html.parser')

        tags = soup('p')

        count = 0

        for tag in tags:
            count += 1

        print("There are {} paragraphs in the webpage at {}".format(count, url))
main()
