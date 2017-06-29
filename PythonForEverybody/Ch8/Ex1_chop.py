empty_str = True

def chop(user_lst):
    if len(user_lst) > 1:
        del user_lst[-1]

    if len(user_lst) > 0:
        del user_lst[0]

    return None

def middle(user_lst):
    end = len(user_lst) - 1
    mid_lst = []

    if len(user_lst) > 1:
        mid_lst = user_lst[1:end]

    return mid_lst

def quit():
    no_answer = True
    quit = None

    while no_answer:
        quit = input("Would you like to quit? (y/n) ")

        try:
            quit = quit[0].lower()
            no_answer = False
        except:
            print ("Invalid entry, please enter 'y' for yes and 'n' for no")

    if quit == 'n':
        return True
    elif quit == 'y':
        return False
    else:
        print ("Neither 'y' nor 'n' found, exiting program.")
        return False

while empty_str:
    user_str = input("Please enter a set of numbers separated by spaces:\n")
    delim = " "

    try:
        orig = user_str.split(delim)
        user_lst = user_str.split(delim)
        empty_str = False
    except:
        print("Invalid entry, please be sure to separate values by spaces.")
        continue

    mid_lst = middle(orig)
    chop(user_lst)

    print ("Your list has been chopped from\n{}\n\nto\n\n{}\n".format(orig, user_lst))
    print ("The middle of your list is\n{}\n".format(mid_lst))
    empty_str = quit()
