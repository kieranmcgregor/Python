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

        elif keep_going == 'n':
            return False

        else:
            print ("Neither 'y' nor 'n' entered, exiting program.")
            return False

def main():
    active = True

    while active:
        reverse_string = ""
        string = input("Please enter a string of characters:\n")
        length = len(string)
        start = 1

        while start <= length:
            next_last = string[-start]

            reverse_string += next_last
            print(next_last, reverse_string)
            start += 1

        active = keep_going()

main()
