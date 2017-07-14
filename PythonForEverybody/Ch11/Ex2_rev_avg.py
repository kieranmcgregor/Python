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
        fname = "mbox.txt"
        fpath = "../Files/" + fname
        fhand = open(fpath)

    return (fname, fhand)

no_quit = True

def line_parser(fhand):
    total = 0
    count = 0

    regex = "New Revision: ([0-9]+)"

    for line in fhand:
        if (re.findall(regex, line)):
            total += int(re.findall(regex, line)[0])
            count += 1

    return (total, count)

while no_quit:
    tot_count = ()

    print ("New Revisions Average Calculator\n")
    fname = input("Please enter just the file name with extension:\n")
    fnfh = open_file(fname)
    fname = fnfh[0]
    fhand = fnfh[1]
    tot_count = line_parser(fhand)
    fhand.close()

    print ("{} had {:.7f} average new revisions\n"
    .format(fname, (tot_count[0]/tot_count[1])))

    no_quit = quit()
