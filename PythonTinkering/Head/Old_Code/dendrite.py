import random
from nerve import Nerve
from nd_meld import Neuron

class Dendrite:

    def __init__(self, name, connection = None):
        self.name = name
        self.propagation_probability = 0.5
        self.signal = 0
        self.connection = self.__connection_initializer(connection)
        self.variability = 0.01

    def __connection_initializer(self, connection):
        if self.name == 'D1' and connection == None:
            V1 = Nerve('V1')
            return [V1]
        else:
            return [connection]

    def __set_probability(self, feedback):
        neutral_signal = 0

        signal = self.signal
        if feedback == '+':
            if signal > neutral_signal:
                self.propagation_probability += random.uniform(0, self.variability)
            elif signal < neutral_signal:
                self.propagation_probability -= random.uniform(0, self.variability)
        elif feedback == '-':
            if signal > neutral_signal:
                self.propagation_probability -= random.uniform(0, self.variability)
            elif signal < neutral_signal:
                self.propagation_probability += random.uniform(0, self.variability)

        stop_propagation_certainty = 0
        continue_propagation_certainty = 1

        if self.propagation_probability < stop_propagation_certainty:
            self.propagation_probability = stop_propagation_certainty
        elif self.propagation_probability > continue_propagation_certainty:
            self.propagation_probability = continue_propagation_certainty

    def __set_signal(self):
        send_continue_propagation = 1
        send_stop_propagation = -1
        self.signal = ((send_continue_propagation) if random.random() <
                        self.propagation_probability else (send_stop_propagation))

    def clean(self, neuron_fp = None):
        stop_propagation_certainty = 0
        dead_neuron = 0

        if neuron_fp == dead_neuron:
            self.connections = []

        elif (self.propagation_probability == stop_propagation_certainty):
            temp_connections = []
            for connection in self.connections:
                if connection.name[0] != 'V':
                    temp_connections.append(connection)

            self.connections = temp_connections

    def propagate(self):
        self.__set_signal()
        signal = self.signal
        print ("{} Signal: {}".format(self.name, signal))
        for connection in self.connection:
            if type(connection) == Nerve:
                if signal == 1:
                    connection.propagate()
            elif type(connection) == Neuron:
                connection.manage_inputs(signal)
            else:
                print ("Not Neuron or Nerve type connection, uh oh!")

    def add_connection(self, connection):
        self.connections.append(connection)

    def adjust_probability(self, feedback):
        self.__set_probability(feedback)
        print ("{} Propagation probability: {}"
                .format(self.name, self.propagation_probability))

    def get_name(self):
        return self.name

    def get_probability(self):
        return self.propagation_probability

    def get_signal(self):
        return self.signal

    def get_score(self):
        return self.score

    def get_connection(self):
        return self.connection

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
