def count(char, string):
    count = 0
    for letter in string:
        if letter.lower() == char:
            count = count + 1

    return count

def keep_going():
    invalid_response = True

    while invalid_response:
        answer = input("Would you like to keep going? (y/n) ")

        try:
            keep_going = answer.lower()[0]
        except:
            print ("Invalid response, please enter 'y' for yes or 'n' for no")
            continue

        if keep_going == 'y':
            return True

        elif keep_going != 'n':
            print ("Neither 'y' nor 'n' entered, exiting program.")

        return False

def main():
    active = True

    while active:
        char = ""
        string = input("Please enter a string:\n")
        not_1_letter = True

        while not_1_letter:
            char = input("Which character would you like counted? ")

            if len(char) == 1:
                not_1_letter = False

            else:
                print("Invalid entry, please enter one (1) character")

        counter = count(char, string)

        if counter == 1:
            print ("'{}' appears in '{}' {} time".format(char, string, counter))

        else:
            print ("'{}' appears in '{}' {} times".format(char, string, counter))

        active = keep_going()

main()
