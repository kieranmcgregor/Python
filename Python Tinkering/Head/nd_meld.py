import random
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
        self.__connections = self.__connections_initializer()
        self.__status = 'ready'
        self.__variability = 0.01
        self.__predendrite_threshold = 10

    def __connections_initializer(self):
        dendrite_name = "D" + str(self.__dendrite_count)
        new_dendrite = Dendrite(dendrite_name)
        self.__dendrite_count += 1
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

    def construct_predendrite(self, neuron, feedback):
        predendrite_absent = True
        predendrite_links = [neuron]

        for connection in self.__connections:
            for connections_connection in connection.get_connections():
                if connections_connection == neuron:
                    predendrite_absent = False
                    if type(connection) == PreDendrite:
                        predendrite = connection
                        predendrite.adjust_score(feedback)
                elif type(connections_connection) == Nerve:
                    if type(connection) == Dendrite:
                        dendrite = connection
                        if dendrite.get_signal() == 1:
                            print (dendrite.get_name(), dendrite.get_connections())
                        else:
                            predendrite_absent = False

        if (predendrite_absent) and (feedback == '+'):
            print (predendrite_links)
            self.add_predendrite(predendrite_links)

    def add_predendrite(self, connection):
        predendrite_name = ''

        if len(self.__dead_predendrites) == 0:
            predendrite_name = "P" + str(self.__predendrite_count)
            self.__predendrite_count += 1
        else:
            predendrite_name = self.__dead_predendrites[0]

        new_predendrite = PreDendrite(predendrite_name, connection)
        self.__connections.append(new_predendrite)

    def add_dendrite(self, connection):
        dendrite_name = ''

        if len(self.__dead_dendrites) == 0:
            dendrite_name = "D" + str(self.__dendrite_count)
            self.__dendrite_count += 1
        else:
            dendrite_name = self.__dead_dendrites[0]

        new_dendrite = Dendrite(dendrite_name, connection)
        self.__connections.append(new_dendrite)

    def clean(self):
        self.__reset()

        temp_dendrites = []
        temp_predendrites = []

        for connection in self.__connections:
            if type(connection) ==  Dendrite:
                dendrite = connection
                dendrite.clean(self.__activation_probability)

                if len(dendrite.get_connections()) > 0:
                    temp_dendrites.append(dendrite)
                else:
                    self.__dead_dendrites.append(dendrite.get_name())

            elif type(connection) == PreDendrite:
                predendrite = connection

                if self.__activation_probability > 0:
                    if predendrite.get_score() >= self.__predendrite_threshold:
                        self.add_dendrite(predendrite.get_connections())
                        self.__dead_predendrites.append(predendrite.get_name())

                    elif predendrite.get_score() <= 0:
                        self.__dead_predendrites.append(predendrite.get_name())

                    else:
                        temp_predendrites.append(predendrite)

        self.__connections = temp_predendrites + temp_dendrites

    def activate(self):
        if self.__status == 'ready':
            self.__status = 'busy'
            print ("{} activated".format(self.__name))
            for connection in self.__connections:
                if type(connection) == Dendrite:
                    dendrite = connection
                    dendrite.propagate()

    def adjust_probability(self, feedback, state):
        self.__set_probability(feedback, state)
        print ("{} firing probability: {}"
                .format(self.__name, self.__activation_probability))
        print ("{} {}".format(self.__name, len(self.__connections)))

        for connection in self.__connections:
            if type(connection) == Dendrite:
                dendrite = connection
                dendrite.adjust_probability(feedback)

    def manage_inputs(self, input_signal):
        continue_propagation_threshold = 1
        if self.__status == 'ready':
            self.__signal += input_signal
            print ("{} input signal: {}".format(self.__name, self.__signal))
            if self.__signal >= continue_propagation_threshold:
                self.__signal = 0
                self.activate()

    def get_name(self):
        return self.__name

    def get_activation_probability(self):
        return self.__activation_probability

    def get_score(self):
        return self.__score

    def get_connections(self):
        return self.__connections

#### Dendrite Class starts #####
from nerve import Nerve

class Dendrite:
    def __init__(self, name, connections = None):
        self.__name = name
        self.__propagation_probability = 0.5
        self.__signal = 0
        self.__connections = self.__connection_initializer(connections)
        self.__variability = 0.01

    def __connection_initializer(self, connection):
        if self.__name == 'D0' and connection == None:
            V0 = Nerve('V0')
            return [V0]
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

    def add_connection(self, connection):
        self.__connections.append(connection)

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
