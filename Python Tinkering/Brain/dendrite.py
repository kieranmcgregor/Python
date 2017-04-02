import random

class Dendrite:
    def __init__(self):
        self.probability = 0.5
        self.signal = 0
        self.connections = []

    def propagate(self):
        self.__set_signal()
        print ("Signal: {}".format(self.signal))

        feedback = input("Reward or punish? (+ / -) ")
        self.__set_probability(feedback)
        print ("Probability: {}".format(self.probability))

    def get_probability(self):
        return self.probability

    def add_connection(self, connection):
        pass

    def get_signal(self):
        return self.signal

    def __set_probability(self, feedback):
        signal = self.signal
        if feedback == '+':
            if signal > 0:
                self.probability -= random.uniform(0, 0.01)
            elif signal < 0:
                self.probability += random.uniform(0, 0.01)
        elif feedback == '-':
            if signal > 0:
                self.probability += random.uniform(0, 0.01)
            elif signal < 0:
                self.probability -= random.uniform(0, 0.01)

        if self.probability < 0:
            self.probability = 0
        elif self.probability > 1:
            self.probability = 1

    def __set_signal(self):
        self.signal = (1) if random.random() > self.probability else (-1)

# def unit_tests():
#     ### Construct two Dendrite objects
#     D1 = Dendrite()
#     D2 = Dendrite()
#
#     ### Get and display divisor of Neuron N1
#     D1_prob = D1.get_probability()
#     print ("D1 probability: {}".format(D1_prob))
#
#     ### Set and Get signal for Neurons N1 and N2
#     ### TASK TO BE TAKEN OVER BY Dendrite class
#     D1_signal = D1.get_signal()
#     D2_signal = D2.get_signal()
#     print (D1_signal, D2_signal)
#
#     ### Set new Neuron N1 divisor and get Neurons N1 and N2 divisors
#     D1_prob = D1.get_probability()
#     D2_prob = D2.get_probability()
#     print (D1_prob, D2_prob)
#
#     ### Check the probability of positive and negative signal with reward (+)
#     ### and punishment (-)
#     count = 0
#     total = 0
#     while count < 25:
#         D1.propagate()
#         if D1.get_signal() == 1:
#             total += 1
#
#         count += 1
#
#     print ("+ sig: {}%\n- sig: {}%".format(total/count, (count-total)/count))
#
# unit_tests()
