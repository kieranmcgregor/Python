def quit():
    quit = ""
    no_answer = True

    while no_answer:
        answer = input("Would you like to quit? (y/n) ")

        try:
            quit = answer[0].lower()
            no_answer = False
        except:
            print ("Invalid entry please enter 'y' for yes and 'n' for no.")
            continue

    if quit == 'n':
        return True
    elif quit != 'y':
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
    senders = {}
    
    for line in fhand:
        if line.startswith("From "):
            words = line.split()
            if len(words) > 3:
                sender = words[1]
                try:
                    senders[sender] += 1
                except:
                    senders[sender] = 1

    return senders

def dsu(senders):
    dsu_senders = list()
    for sender, count in list(senders.items()):
        dsu_senders.append((count, sender))

    dsu_senders.sort(reverse = True)

    return dsu_senders

while no_quit:
    senders = {}
    fname = input("Please enter just the file name with extension:\n")

    fhand = open_file(fname)
    senders = line_parser(fhand)
    fhand.close()

    dsu_senders = dsu(senders)
    print (dsu_senders[0][1], dsu_senders[0][0])

    no_quit = quit()
