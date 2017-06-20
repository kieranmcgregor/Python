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

empty_fname = True

def search(fhand):
    count = 0
    for line in fhand:
        words = line.split()

        if len(words) < 2 or words[0] != 'From': continue
        print(words[1])
        count += 1

    return count

while empty_fname:
    fname = input("Please enter file path:\n")

    try:
        fhand = open(fname)
    except:
        print("Invalid file path, using default ../Files/mbox-short.txt")
        fname = "../Files/mbox-short.txt"
        fhand = open(fname)

    count = search(fhand)
    print ("There were {} lines in the file with From as the first word"
            .format(count))

    empty_fname = quit()
