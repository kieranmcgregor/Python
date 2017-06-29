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

def search(days_of_week):
    search_on = True

    while search_on:
        search = input("Enter day of the week:\n").title()

        if search in days_of_week:
            print ("{} commits were done on {}".format(days_of_week[search], search))
        else:
            print ("Your search was not found")

        answer = input("Would you like to continue searching? (y/n) ")

        if 'y' in answer.lower():
            continue
        else:
            search_on = False

no_quit = True
days_of_week = {}

while no_quit:
    fname = input("Please enter just the file name with extension:\n")
    fhand = open_file(fname)

    for line in fhand:
        if line.startswith("From "):
            words = line.split()
            if len(words) > 3:
                day_of_week = words[2]
                try:
                    days_of_week[day_of_week] += 1
                except:
                    days_of_week[day_of_week] = 1

    fhand.close()

    print (days_of_week)

    search(days_of_week)

    no_quit = quit()
