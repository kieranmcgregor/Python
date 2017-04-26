import random
from collections import Counter
from predendrite import PreDendrite

class Neuron:
    def __init__(self, name):
        self.__name = name
        self.__predendrite_count = 0
        self.__dendrite_count = 0
        self.__dead_predendrites = []
        self.__dead_dendrites = []
        self.__activation_probability = 0.5
        self.__signal = 0
        self.__status = 'ready'
        self.__variability = 0.01
        self.__predendrite_threshold = 10
        self.__connections = self.__connection_initializer()

    def __connection_initializer(self, connections = None):
        dendrite_name = ''
        dendrite_name = "D" + str(self.__name[1:]) + str(self.__dendrite_count)
        self.__dendrite_count += 1
        new_dendrite = Dendrite(dendrite_name, connections)
        return [new_dendrite]

    def __set_probability(self, feedback, state):
        if feedback == '+':
            if state == 'active':
                self.__activation_probability += random.uniform(0, self.__variability)
            elif state == 'inactive':
                self.__activation_probability -= random.uniform(0, self.__variability)
        elif feedback == '-':
            if state == 'active':
                self.__activation_probability -= random.uniform(0, self.__variability)
            elif state == 'inactive':
                self.__activation_probability += random.uniform(0, self.__variability)

        rest_certainty = 0
        activate_certainty = 1

        if self.__activation_probability < rest_certainty:
            self.__activation_probability = rest_certainty
        elif self.__activation_probability > activate_certainty:
            self.__activation_probability = activate_certainty

    def __reset(self):
        self.__status = 'ready'
        self.__signal = 0

    def activate(self):
        if self.__status == 'ready':
            self.__status = 'busy'
            print ("{} activated".format(self.__name))
            for connection in self.__connections:
                if type(connection) == Dendrite:
                    dendrite = connection
                    dendrite.propagate()

    def manage_inputs(self, input_signal):
        continue_propagation_threshold = 1
        if self.__status == 'ready':
            self.__signal += input_signal
            print ("{} input signal: {}".format(self.__name, self.__signal))
            if self.__signal >= continue_propagation_threshold:
                self.__signal = 0
                self.activate()

    def adjust_probability(self, feedback, state):
        self.__set_probability(feedback, state)
        print ("{} firing probability: {}"
                .format(self.__name, self.__activation_probability))
        print ("{} {}".format(self.__name, len(self.__connections)))
        print ("{}".format(self.__connections))

        for connection in self.__connections:
            if type(connection) == Dendrite:
                dendrite = connection
                dendrite.adjust_probability(feedback)

    def construct_predendrite(self, other_activated_neurons, feedback):
        neurons_absent = True
        # all_elements_absent = True
        activated_elements = other_activated_neurons
        for connection in self.get_connections():
            if Counter(connection.get_connections()) == Counter(other_activated_neurons):
                # print ("match {}".format(connection.get_connections()))
                neurons_absent = False
                if type(connection) == PreDendrite:
                    predendrite = connection
                    predendrite.adjust_score(feedback)

        # print (other_activated_neurons, activated_nerves, activated_elements)
        if ((neurons_absent) and (feedback == '+')):
            if len(other_activated_neurons) > 0:
                self.add_predendrite(other_activated_neurons)

    def clean(self):
        self.__reset()

        temp_dendrites = []
        temp_predendrites = []

        if self.__activation_probability > 0:
            for connection in self.__connections:
                print ("{} connection {}".format(self.__name, connection))
                if type(connection) == Dendrite:
                    dendrite = connection
                    dendrite.clean(self.__activation_probability)

                    if len(dendrite.get_connections()) > 0:
                        temp_dendrites.append(dendrite)
                    else:
                        self.__dead_dendrites.append(dendrite.get_name())

                elif type(connection) == PreDendrite:
                    predendrite = connection
                    if predendrite.get_score() >= self.__predendrite_threshold:
                        self.add_dendrite(predendrite.get_connections())
                        self.__dead_predendrites.append(predendrite.get_name())

                    elif predendrite.get_score() <= 0:
                        self.__dead_predendrites.append(predendrite.get_name())

                    else:
                        temp_predendrites.append(predendrite)

        self.__connections = temp_predendrites + temp_dendrites

    def add_predendrite(self, connections):
        predendrite_name = ''

        if len(self.__dead_predendrites) == 0:
            predendrite_name = "P" + str(self.__predendrite_count)
            self.__predendrite_count += 1
        else:
            predendrite_name = self.__dead_predendrites[0]
            self.__dead_predendrites.pop(0)

        new_predendrite = PreDendrite(predendrite_name, connections)
        self.__connections.append(new_predendrite)

    def add_dendrite(self, connections = None):
        dendrite_name = ''
        if len(self.__dead_dendrites) == 0:
            dendrite_name = "D" + str(self.__name[1:]) + str(self.__dendrite_count)
            self.__dendrite_count += 1
        else:
            dendrite_name = self.__dead_dendrites[0]

        new_dendrite = Dendrite(dendrite_name, connections)
        self.__connections.append(new_dendrite)

    def get_name(self):
        return self.__name

    def get_activation_probability(self):
        return self.__activation_probability

    def get_score(self):
        return self.__score

    def get_connections(self):
        return self.__connections

    def get_activated_nerves(self):
        activated_nerves = []
        for connection in self.get_connections():
            if type(connection) == Dendrite:
                dendrite = connection
                if dendrite.get_signal() == 1:
                    if type(dendrite.get_connections()[0]) == Nerve:
                        for nerve in dendrite.get_connections():
                            if nerve not in activated_nerves:
                                activated_nerves.append(nerve)
        # print ("activated_nerves {}".format(activated_nerves))
        return activated_nerves

#### Dendrite Class starts #####
from nerve import Nerve

class Dendrite:
    def __init__(self, name, connections = None):
        self.__name = name
        self.__nerve_count = 0
        self.__propagation_probability = 0.5
        self.__signal = 0
        self.__connections = self.__connection_initializer(connections)
        self.__variability = 0.01

    def __connection_initializer(self, connections):
        if connections == None:
            nerve_name = ''

            nerve_name = "V" + str(self.__name[1:]) + str(self.__nerve_count)
            self.__nerve_count += 1

            new_nerve = Nerve(nerve_name)
            return [new_nerve]
        else:
            return connections

    def __set_probability(self, feedback):
        neutral_signal = 0

        signal = self.__signal
        if feedback == '+':
            if signal > neutral_signal:
                self.__propagation_probability += random.uniform(0, self.__variability)
            elif signal < neutral_signal:
                self.__propagation_probability -= random.uniform(0, self.__variability)
        elif feedback == '-':
            if signal > neutral_signal:
                self.__propagation_probability -= random.uniform(0, self.__variability)
            elif signal < neutral_signal:
                self.__propagation_probability += random.uniform(0, self.__variability)

        stop_propagation_certainty = 0
        continue_propagation_certainty = 1

        if self.__propagation_probability < stop_propagation_certainty:
            self.__propagation_probability = stop_propagation_certainty
        elif self.__propagation_probability > continue_propagation_certainty:
            self.__propagation_probability = continue_propagation_certainty

    def __set_signal(self):
        send_continue_propagation = 1
        send_stop_propagation = -1
        self.__signal = ((send_continue_propagation) if random.random() <
                        self.__propagation_probability else (send_stop_propagation))

    def __reset(self):
        self.__signal = 0

    def clean(self, neuron_ap = None):
        self.__reset()

        stop_propagation_certainty = 0
        dead_neuron = 0
        temp_connections = []

        if neuron_ap == dead_neuron:
            self.__connections = []
        else:
            for connection in self.__connections:
                if connection.get_name()[0] == 'V':
                    if (self.__propagation_probability > stop_propagation_certainty):
                        temp_connections.append(connection)
                        connection.clean()
            self.__connections = temp_connections

    def propagate(self):
        self.__set_signal()
        signal = self.__signal
        print ("{} Signal: {}".format(self.__name, signal))
        for connection in self.__connections:
            if type(connection) == Nerve:
                if signal == 1:
                    connection.propagate()
            elif type(connection) == Neuron:
                connection.manage_inputs(signal)
            else:
                print ("Not Neuron or Nerve type connection, uh oh!")

    def adjust_probability(self, feedback):
        self.__set_probability(feedback)
        print ("{} Propagation probability: {}"
                .format(self.__name, self.__propagation_probability))

    def get_name(self):
        return self.__name

    def get_probability(self):
        return self.__propagation_probability

    def get_signal(self):
        return self.__signal

    def get_connections(self):
        return self.__connections
