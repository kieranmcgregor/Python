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

def open_file(fname):
    fpath = "../Files/" + fname
    try:
        fhand = open(fpath)
    except:
        print("Invalid file path, using default ../Files/mbox-short.txt")
        fpath = "../Files/mbox-short.txt"
        fhand = open(fpath)

    return fhand

no_quit = True

def line_parser(fhand):
    hours = []

    for line in fhand:
        hour = re.findall('^From.* ([0-9][0-9]):', line)
        if len(hour) > 0:
            print(line)
            hours.append(hour)

    return hours

while no_quit:
    senders = {}
    fname = input("Please enter just the file name with extension:\n")

    fhand = open_file(fname)
    hours = line_parser(fhand)
    fhand.close()

    for hour in hours:
        print(hour[0])

    no_quit = quit()
