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
        print("Invalid file path, using default ../Files/mbox.txt")
        fpath = "../Files/mbox.txt"
        fhand = open(fpath)

    return fhand

no_quit = True

def line_parser(fhand, regex):
    count = 0
    for line in fhand:
        if re.findall(regex, line):
            count += 1

    return count

while no_quit:
    count = 0;
    fname = input("Please enter just the file name with extension:\n")
    fhand = open_file(fname)

    regex = input("Enter a regular expression to search for in the file:\n")
    count = line_parser(fhand, regex)
    fhand.close()

    print ("{} had {} lines that matched {}\n".format(fname, count, regex))

    no_quit = quit()
