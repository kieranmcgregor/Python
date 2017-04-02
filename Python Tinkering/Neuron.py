import random

class Neuron:
    def __init__(self):
        self.divisor = 0.5
        self.signal = 0
        self.connections = []

    def get_divisor(self):
        return self.divisor

    def set_divisor(self, feedback):
        signal = self.signal
        if feedback == '+':
            if signal > 0:
                self.divisor += random.uniform(0, 0.1)
            elif signal < 0:
                self.divisor -= random.uniform(0, 0.1)
        elif feedback == '-':
            if signal > 0:
                self.divisor -= random.uniform(0, 0.1)
            elif signal < 0:
                self.divisor += random.uniform(0, 0.1)

        if self.divisor < 0:
            self.divisor = 0.000000000000001

        self.signal = 0

    def get_signal(self):
        return self.signal

    def set_signal(self):
        self.signal = (1) if random.random() > self.divisor else (-1)

def unit_tests():
    ### Construct two Neuron objects
    N1 = Neuron()
    N2 = Neuron()

    ### Get and display divisor of Neuron N1
    N1_divisor = N1.get_divisor()
    print (N1_divisor)

    ### Set and Get signal for Neurons N1 and N2
    ### TASK TO BE TAKEN OVER BY Dendrite class
    N1.set_signal()
    N2.set_signal()
    N1_signal = N1.get_signal()
    N2_signal = N2.get_signal()
    print (N1_signal, N2_signal)

    ### Set new Neuron N1 divisor and get Neurons N1 and N2 divisors
    N1.set_divisor('+')
    N1_divisor = N1.get_divisor()
    N2_divisor = N2.get_divisor()
    print (N1_divisor, N2_divisor)

    ### Check the probability of positive and negative signal with reward (+)
    ### and punishment (-)
    count = 0
    total = 0
    while count < 50:
        change = input("Reward or punish? (+ / -) ")
        N1.set_divisor(change)
        N1_divisor = N1.get_divisor()
        print ("N1 divisor: {}".format(N1_divisor))
        N1.set_signal()
        N1_signal = N1.get_signal()
        print ("Signal: {}".format(N1_signal))
        if N1_signal == 1:
            total += 1

        count += 1

    print ("+ sig: {}%\n- sig: {}%".format(total/count, (count-total)/count))

unit_tests()
