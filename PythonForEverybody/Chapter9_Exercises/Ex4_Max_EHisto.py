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

while no_quit:
    email_addresses = {}
    fname = input("Please enter just the file name with extension:\n")
    fhand = open_file(fname)

    for line in fhand:
        if line.startswith("From "):
            words = line.split()
            if len(words) > 3:
                email_address = words[1]
                try:
                    email_addresses[email_address] += 1
                except:
                    email_addresses[email_address] = 1

    fhand.close()

    print(email_addresses)
    maximum = max(email_addresses.values())
    for email, count in email_addresses.items():
        if count == maximum:
            print (email, maximum)

    no_quit = quit()
