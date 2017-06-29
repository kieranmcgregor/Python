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
        print("Invalid file path, using default ../Files/words.txt")
        fpath = "../Files/words.txt"
        fhand = open(fpath)

    return fhand

def reset_check():
    reset = ""
    no_answer = True

    while no_answer:
        answer = input("Would you like to reset? (y/n) ")

        try:
            reset = answer[0].lower()
            no_answer = False
        except:
            print ("Invalid entry please enter 'y' for yes and 'n' for no.")
            continue

    if reset == 'n':
        return False
    elif reset != 'y':
        print ("Neither 'y' nor 'n' found, resetting program")

    return True

no_quit = True
fname = None
word_places = {}
count = 0
reset = True

while no_quit:
    if fname == None or reset:
        word_places = {}
        fname = input("Please enter just the file name with extension:\n")
        fhand = open_file(fname)

        for line in fhand:
            words = line.split(" ")
            for word in words:
                word = word.strip("\n\\{}")
                if len(word) > 0:
                    if word in word_places:
                        word_places[word].append(count)
                    else:
                        word_places[word] = [count]

                    count += 1

    print (word_places)

    search = input("Enter a word string to search in the above list:\n")

    if search in word_places:
        print ("'{}' can be found at positions {}".format(search, word_places[search]))
    else:
        print ("Your word string was not found")

    no_quit = quit()
    if no_quit:
        reset = reset_check()
