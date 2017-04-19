import random
from nd_meld import Neuron

class Cerebra:
    def __init__(self, name):
        self.__name = name
        self.__neurons = self.__primordial_brain()

    def __primordial_brain(self):
        neurons = []
        initial_neuron_count = 4
        index = 0

        while index < initial_neuron_count:
            neuron_name = "N" + str(index)
            new_neuron = Neuron(neuron_name)
            neurons.append(new_neuron)
            index += 1

        return neurons

    def __feedback_input(self, activated_neurons):
        feedback = input("Reward or punish? (+ / -) ")
        for neuron in self.__neurons:
            if neuron in activated_neurons:
                neuron.adjust_probability(feedback, 'active')
            else:
                neuron.adjust_probability(feedback, 'inactive')

        return feedback

    def __construct_predendrites(self, activated_neurons, feedback):
        for neuron1 in activated_neurons:
            for neuron2 in activated_neurons:
                if neuron1 != neuron2:
                    neuron1.construct_predendrite(neuron2, feedback)

    def activate(self):
        activated_neurons = []
        activate = 1
        rest = 0

        for neuron in self.__neurons:
            activation_probability = neuron.get_activation_probability()
            signal = ((activate) if random.random() <
                        activation_probability else (rest))
            if signal == activate:
                neuron.activate()
                activated_neurons.append(neuron)

        feedback = self.__feedback_input(activated_neurons)
        self.__construct_predendrites(activated_neurons, feedback)

    def clean(self):
        temp_neurons = []
        for neuron in self.__neurons:
            neuron.clean()
            if len(neuron.get_connections()) != 0:
                temp_neurons.append(neuron)

        self.__neurons = temp_neurons

    def add_neurons(self):
        neuron_name = "N" + str(len(self.__neurons))
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
