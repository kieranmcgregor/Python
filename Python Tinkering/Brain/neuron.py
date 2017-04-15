import random
from dendrite import Dendrite

class Neuron:
    def __init__(self, name):
        self.name = name
        self.firing_probability = 0.5
        self.signal = 0
        self.score = 0
        self.dendrites = self.__born()

    def __born(self):
        D1 = Dendrite('D1')
        return [D1]

    def __set_probability(self, feedback, state):
        if feedback == '+':
            if state == 'active':
                self.firing_probability -= random.uniform(0, 0.01)
            elif state == 'inactive':
                self.firing_probability += random.uniform(0, 0.01)
        elif feedback == '-':
            if state == 'active':
                self.firing_probability += random.uniform(0, 0.01)
            elif state == 'inactive':
                self.firing_probability -= random.uniform(0, 0.01)

        lowest_probability = 0
        highest_probability = 1

        if self.firing_probability < lowest_probability:
            self.firing_probability = lowest_probability
        elif self.firing_probability > highest_probability:
            self.firing_probability = highest_probability

    def add_connection(self, dendrite, neuron = None):
        self.dendrites.append(dendrite)
        if neuron != None:
            dendrite.add_connection(neuron)

    def clean(self):
        for dendrite in self.dendrites:
            dendrite.clean()
            if len(dendrite.connections) == 0:
                self.kill_dendrite(dendrite.name)

    def propagate(self):
        for dendrite in self.dendrites:
            dendrite.propagate()

    def kill_dendrite(self, name):
        temp_dendrites = []
        for dendrite in self.dendrites:
            if dendrite.name != name:
                temp_dendrites.append(dendrite)

        self.dendrites = temp_dendrites

    def adjust_score(self, feedback, state):
        if feedback == "+":
            self.score = 0
        elif feedback == "-":
            self.score += 1
        print ("{} score: {}".format(self.name, self.score))

        self.__set_probability(feedback, state)
        print ("{} firing probability: {}"
                .format(self.name, self.firing_probability))

        for dendrite in self.dendrites:
            dendrite.adjust_score(feedback)

    def manage_inputs(self, input_signal):
        continue_propagation_threshold = 1
        signal = self.signal
        signal += input_signal
        print ("Input signal: {}".format(signal))
        if signal >= continue_propagation_threshold:
            self.propagate()

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_firing_probability(self):
        return self.firing_probability

# def unit_tests():
#     ### Construct two Neuron objects
#     D1 = Dendrite()
#     V1 = Nerve()
#     N1 = Neuron()
#     N2 = Neuron()
#
#     N1.add_connection(D1)
#     N2.add_connection(V1)
#
#     total = 0
#     count = 0
#
#     while count < 50:
#         N1.propagate()
#         if D1.get_signal() == 1:
#             V1_output = V1.get_output()
#             print ("V1 ouput: {}".format(V1_output))
#             total += 1
#         count += 1
#
#     print ("+ sig: {}%\n- sig: {}%\n*From Neuron"
#             .format(total/count, (count-total)/count))
#
# unit_tests()
