from brain import Brain
from neuron import Neuron
from dendrite import Dendrite
from nerve import Nerve

def build_brain():
    build = input("Would you like to start? (y/n)\n")
    if build[0].lower() == 'y':
        B1 = Brain("B1")
        return B1

    elif build[0].lower() == 'n':
        return None

def main():
    run = True
    brain = build_brain()
    # rounds = 0
    threshold = 10 # Randomly chosen magic number

    if brain == None:
        run = False

    while run:
        brain.clean()
        # if rounds >= threshold:
        #     rounds = 0
        #     brain.add_neurons()

        if len(brain.neurons) > 0:
            action = input("Would you like to activate or quit (a/q)\n")
            if action[0].lower() == 'a':
                brain.activate()
            elif action[0].lower() == 'q':
                run = False
        else:
            run = False
            print ("Your artificial brain has become dead. We hope you enjoyed!")

        # rounds += 1

main()
