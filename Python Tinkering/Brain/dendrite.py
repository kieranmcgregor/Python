from nerve import Nerve
import random

class Dendrite:
    def __init__(self, name):
        self.name = name
        self.propagation_probability = 0.5
        self.signal = 0
        self.score = 0
        self.connections = self.__born()

    def __born(self):
        if self.name == 'D1':
            V1 = Nerve('V1')
            return [V1]

    def __set_probability(self, feedback):
        signal_mean = 0

        signal = self.signal
        if feedback == '+':
            if signal > signal_mean:
                self.propagation_probability -= random.uniform(0, 0.01)
            elif signal < signal_mean:
                self.propagation_probability += random.uniform(0, 0.01)
        elif feedback == '-':
            if signal > signal_mean:
                self.propagation_probability += random.uniform(0, 0.01)
            elif signal < signal_mean:
                self.propagation_probability -= random.uniform(0, 0.01)

        lowest_probability = 0
        highest_probability = 1

        if self.propagation_probability < lowest_probability:
            self.propagation_probability = lowest_probability
        elif self.propagation_probability > highest_probability:
            self.propagation_probability = highest_probability

    def __set_signal(self):
        send_continue_propagation = 1
        send_stop_propagation = -1
        self.signal = ((send_continue_propagation) if random.random() >
                        self.propagation_probability else (send_stop_propagation))

    def clean(self, name = None):
        non_firing = 1
        if self.propagation_probability == non_firing:
            temp_connections = []
            for connection in self.connections:
                if connection.name[0] != 'V':
                    temp_connections.append(connection)

            self.connections = temp_connections

        else:
            temp_connections = []
            for connection in self.connections:
                if connection.name[0] != name:
                    temp_connections.append(connection)

            self.connections = temp_connections

    def propagate(self):
        self.__set_signal()
        signal = self.signal
        print ("{} Signal: {}".format(self.name, signal))
        for connection in self.connections:
            if type(connection) == Nerve:
                if signal == 1:
                    connection.propagate()
            elif type(connection) == Neuron:
                connection.manage_inputs(signal)
            else:
                print ("Not Neuron or Nerve type connection, uh oh!")

    def add_connection(self, connection):
        self.connections.append(connection)

    def adjust_score(self, feedback):
        if feedback == "+":
            self.score = 0
        elif feedback == "-":
            self.score += 1

        print ("{} score: {}".format(self.name, self.score))

        self.__set_probability(feedback)
        print ("Probability: {}".format(self.propagation_probability))

    def get_probability(self):
        return self.probability

    def get_signal(self):
        return self.signal

    def get_score(self):
        return self.score

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
