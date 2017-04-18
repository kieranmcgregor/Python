from cerebra import Cerebra

def build_cerebra():
    build = input("Would you like to start? (y/n)\n")
    if build[0].lower() == 'y':
        return Cerebra("C1")

    elif build[0].lower() == 'n':
        return None

def main():
    run = True
    cerebra = build_cerebra()
    # rounds = 0
    threshold = 10 # Randomly chosen magic number

    if cerebra == None:
        run = False

    while run:
        cerebra.clean()
        # if rounds >= threshold:
        #     rounds = 0
        #     cerebra.add_neurons()

        if len(cerebra.get_neurons()) > 0:
            action = input("Would you like to activate or quit (a/q)\n")
            try:
                if action[0].lower() == 'a':
                    cerebra.activate()
                elif action[0].lower() == 'q':
                    run = False
            except:
                print ("\'{}\' is an invalid entry, entry ignored."
                        .format(action))
        else:
            run = False
            print ("Your brain is dead. We hope you enjoyed!")

        # rounds += 1

main()
