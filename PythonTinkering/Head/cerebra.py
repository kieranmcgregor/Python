import random
from collections import Counter
from preneuron import PreNeuron
from nd_meld import Neuron

class Cerebra:
    def __init__(self, name, number_of_neurons):
        self.__name = name
        self.__neuron_count = 0
        self.__neurons = self.__primordial_brain(number_of_neurons)
        self.__preneuron_threshold = 10
        self.__dead_preneurons = []

    def __primordial_brain(self, number_of_neurons):
        neurons = []
        initial_neuron_count = number_of_neurons

        while self.__neuron_count < initial_neuron_count:
            neuron_name = "N" + str(self.__neuron_count)
            new_neuron = Neuron(neuron_name)
            neurons.append(new_neuron)
            self.__neuron_count += 1

        return neurons

    def __feedback_input(self, activated_neurons):
        feedback = input("Reward or punish? (+ / -) ")
        for neuron in self.__neurons:
            if type(neuron) == Neuron:
                if neuron in activated_neurons:
                    neuron.adjust_probability(feedback, 'active')
                else:
                    neuron.adjust_probability(feedback, 'inactive')

        return feedback

    def __construct_preneurons(self, activated_neurons, feedback):
        activated_nerves = []
        for neuron in activated_neurons:
            activated_nerves = neuron.get_activated_nerves()

        for neuron in self.__neurons:
            for connection in neuron.get_connections():
                if (type(neuron) == Neuron):
                    if (activated_nerves != connection.get_connections()) and (feedback == '+'):
                        self.add_preneuron(activated_nerves)
                if (type(connection) == PreNeuron):
                    if activated_nerves == connection.get_connections():
                        connection.adjust_score(feedback)


    def __construct_predendrites(self, activated_neurons, feedback):
        for neuron1 in activated_neurons:
            other_activated_neurons = []
            for neuron2 in activated_neurons:
                if neuron1 != neuron2:
                    other_activated_neurons.append(neuron2)
            neuron1.construct_predendrite(other_activated_neurons, feedback)

    def activate(self):
        activated_neurons = []
        activate = 1
        rest = 0
        for neuron in self.__neurons:
            if type(neuron) == Neuron:
                activation_probability = neuron.get_activation_probability()
                signal = ((activate) if random.random() <
                            activation_probability else (rest))
                if signal == activate:
                    neuron.activate()
                    activated_neurons.append(neuron)

        feedback = self.__feedback_input(activated_neurons)
        self.__construct_preneurons(activated_neurons, feedback)
        self.__construct_predendrites(activated_neurons, feedback)

    def clean(self):
        temp_neurons = []
        temp_preneurons = []
        for neuron in self.__neurons:
            if type(neuron) == Neuron:
                neuron.clean()
                if len(neuron.get_connections()) != 0:
                    temp_neurons.append(neuron)
            elif type(neuron) == PreNeuron:
                preneuron = neuron
                if preneuron.get_score() >= self.__preneuron_threshold:
                    self.add_neuron(preneuron.get_connections())
                    self.__dead_preneurons.append(preneuron.get_name())

                elif preneuron.get_score() <= 0:
                    self.__dead_preneurons.append(preneuron.get_name())

                else:
                    temp_preneurons.append(preneuron)

        self.__neurons = temp_neurons + temp_preneurons

    def add_preneuron(self, connections):
        preneuron_name = "PN" + str(self.__neuron_count)
        new_preneuron = PreNeuron(preneuron_name, connections)
        self.__neurons.append(new_preneuron)

    def add_neuron(self):
        neuron_name = "N" + str(self.__neuron_count)
        new_neuron = Neuron(neuron_name)
        self.__neurons.append(new_neuron)

    def get_neurons(self):
        return self.__neurons

# def unit_tests():
#     ### Construct two Neuron objects
#     D1 = Dendrite("D1")
#     V1 = Nerve("V1")
#     V2 = Nerve("V2")
#     N1 = Neuron("N1")
#     N2 = Neuron("N2")
#
#     N1.add_connection(D1, N2)
#     N1.add_connection(V1)
#     N2.add_connection(V2)
#
#     total = 0
#     count = 0
#
#     while count < 50:
#         N1.self_propagate()
#         if D1.get_signal() == 1:
#             total += 1
#         count += 1
#
#     print ("+ sig: {}%\n- sig: {}%\n*From Neuron"
#             .format(total/count, (count-total)/count))
#
# unit_tests()
