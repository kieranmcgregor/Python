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

while empty_fname:
    found_words = {}
    fname = input("Please enter file path:\n")

    try:
        fhand = open(fname)
    except:
        print("Invalid file path, using default ..\Files\\romeo.txt")
        fname = "../Files/romeo.txt"
        fhand = open(fname)

    for line in fhand:
        poem_words = line.split()

        for word in poem_words:

            word = word.lower()

            try:
                found_words[word] += 1
            except:
                found_words[word] = 1

    print ("The words found in the poem and their frequency are\n {}"
            .format(found_words))

    empty_fname = quit()
