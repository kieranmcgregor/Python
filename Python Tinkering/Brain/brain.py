import random
from neuron import Neuron

class Brain:
    def __init__(self, name):
        self.name = name
        self.neurons = self.__primordial_brain()

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

    def activate(self):
        activated_neurons = []
        for neuron in self.neurons:
            firing_probability = neuron.get_firing_probability()
            signal = (1) if random.random() > firing_probability else (0)
            if signal == 1:
                neuron.propagate()
                activated_neurons.append(neuron)

        feedback = input("Reward or punish? (+ / -) ")
        for neuron in self.neurons:
            if neuron in activated_neurons:
                neuron.adjust_score(feedback, 'active')
            else:
                neuron.adjust_score(feedback, 'inactive')

    def clean(self):
        for neuron in self.neurons:
            neuron.clean()
            if len(neuron.dendrites) == 0:
                self.kill_neuron(neuron.name)

    def kill_neuron(self, name):
        temp_neurons = []
        for neuron in self.neurons:
            if neuron.get_name() != name:
                temp_neurons.append(neuron)
            # else:
            #     ###dendrite.clean(neuron.name)
            #     print ("No way to erase from dendrite")

        self.neurons = temp_neurons

    def add_neurons(self):
        neuron_name = "N" + str(len(self.neurons))
        new_neuron = Neuron(neuron_name)
        self.neurons.append(new_neuron)

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
