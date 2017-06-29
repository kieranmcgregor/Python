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
    hours = {}

    for line in fhand:
        if line.startswith("From "):
            words = line.split()
            if len(words) > 3:
                time = words[5]
                hour = time.split(':')[0]
                try:
                    hours[hour] += 1
                except:
                    hours[hour] = 1

    return hours

def dsu(hours):
    dsu_hours = list()
    for hour, count in list(hours.items()):
        dsu_hours.append((hour, count))

    dsu_hours.sort()

    return dsu_hours

while no_quit:
    senders = {}
    fname = input("Please enter just the file name with extension:\n")

    fhand = open_file(fname)
    hours = line_parser(fhand)
    fhand.close()

    dsu_hours = dsu(hours)

    for hour in dsu_hours:
        print(hour[0], hour[1])

    no_quit = quit()
