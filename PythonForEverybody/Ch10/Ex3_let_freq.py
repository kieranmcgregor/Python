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
        print("Invalid file path, using default ../Files/romeo.txt")
        fpath = "../Files/romeo.txt"
        fhand = open(fpath)

    return fhand

no_quit = True

def parser(fhand):
    letters = list()
    for line in fhand:
        letters += list(line)

    return letters

def array_builder(letters):
    # If only for English using the alphabet for a
    # positive would suffice but in order to account for
    # letters of other alphabets, exclusion of punctuation
    # can be used

    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    excluded = '~`!@#$%^&*()-_=+][}{|/\?.><, \n\t'
    let_freq = {}

    for letter in letters:
        # letter = letter.lower()
        if letter not in excluded:
            letter = letter.lower()
            try:
                let_freq[letter] += 1
            except:
                let_freq[letter] = 1

    return let_freq

def dsu(let_freq):
    dsu_lf = list()
    for letter, count in list(let_freq.items()):
        dsu_lf.append((letter, count))

    dsu_lf.sort()

    return dsu_lf

while no_quit:
    senders = {}
    fname = input("Please enter just the file name with extension:\n")

    fhand = open_file(fname)
    letters = parser(fhand)
    fhand.close()

    let_freq = array_builder(letters)
    dsu_lf = dsu(let_freq)

    for let_count in dsu_lf:
        print(let_count[0], let_count[1])

    no_quit = quit()
