import random
from predendrite import PreDendrite

class Neuron:
    def __init__(self, name):
        self.name = name
        self.predendrite_count = 0
        self.dendrite_count = 0
        self.dead_predendrites = []
        self.dead_dendrites = []
        self.activation_probability = 0.5
        self.signal = 0
        self.connections = self.__connections_initializer()
        self.status = 'ready'
        self.variability = 0.01
        self.predendrite_threshold = 10

    def __connections_initializer(self):
        dendrite_name = "D" + str(self.dendrite_count)
        new_dendrite = Dendrite(dendrite_name)
        self.dendrite_count += 1
        return [new_dendrite]

    def __set_probability(self, feedback, state):
        if feedback == '+':
            if state == 'active':
                self.activation_probability += random.uniform(0, self.variability)
            elif state == 'inactive':
                self.activation_probability -= random.uniform(0, self.variability)
        elif feedback == '-':
            if state == 'active':
                self.activation_probability -= random.uniform(0, self.variability)
            elif state == 'inactive':
                self.activation_probability += random.uniform(0, self.variability)

        rest_certainty = 0
        activate_certainty = 1

        if self.activation_probability < rest_certainty:
            self.activation_probability = rest_certainty
        elif self.activation_probability > activate_certainty:
            self.activation_probability = activate_certainty

    def __reset(self):
        self.status = 'ready'
        self.signal = 0

    def check_connections(self, neuron, feedback):
        connection_absent = True
        for connection in self.connections:
            for connections_connection in connection.get_connection():
                if connections_connection == neuron:
                    if type(connection) == Dendrite:
                        connection_absent = False

                    elif type(connection) == PreDendrite:
                        predendrite = connection
                        predendrite.adjust_score(feedback)
                        connection_absent = False
                elif connection.get_connection() == Nerve:
                    connection_absent = False

        return connection_absent

    def add_predendrite(self, connection):
        predendrite_name = ''

        if len(self.dead_predendrites) == 0:
            predendrite_name = "P" + str(self.predendrite_count)
            self.predendrite_count += 1
        else:
            predendrite_name = self.dead_predendrites[0]

        new_predendrite = PreDendrite(predendrite_name, connection)
        self.connections.append(new_predendrite)

    def add_dendrite(self, connection):
        dendrite_name = ''

        if len(self.dead_dendrites) == 0:
            dendrite_name = "D" + str(self.dendrite_count)
            self.dendrite_count += 1
        else:
            dendrite_name = self.dead_dendrites[0]

        new_dendrite = Dendrite(dendrite_name, connection)
        self.connections.append(new_dendrite)

    def clean(self):
        temp_dendrites = []
        temp_predendrites = []

        for connection in self.connections:
            if type(connection) ==  Dendrite:
                dendrite = connection
                dendrite.clean(self.activation_probability)

                if len(dendrite.get_connection()) > 0:
                    temp_dendrites.append(dendrite)
                else:
                    self.dead_dendrites.append(dendrite.get_name())

            elif type(connection) == PreDendrite:
                predendrite = connection

                if self.activation_probability > 0:
                    if predendrite.get_score() >= self.predendrite_threshold:
                        for connection in predendrite.get_connection():
                            self.add_dendrite(connection)
                        self.dead_predendrites.append(predendrite.get_name())

                    elif predendrite.get_score() <= 0:
                        self.dead_predendrites.append(predendrite.get_name())

                    else:
                        temp_predendrites.append(predendrite)

        self.connections = temp_predendrites + temp_dendrites

    def activate(self):
        if self.status == 'ready':
            self.status = 'busy'
            print ("{} activated".format(self.name))
            for connection in self.connections:
                if type(connection) == Dendrite:
                    dendrite = connection
                    dendrite.propagate()

    def adjust_probability(self, feedback, state):
        self.__reset()
        self.__set_probability(feedback, state)
        print ("{} firing probability: {}"
                .format(self.name, self.activation_probability))
        print ("{} {}".format(self.name, len(self.connections)))

        for connection in self.connections:
            if type(connection) == Dendrite:
                dendrite = connection
                dendrite.adjust_probability(feedback)

    def manage_inputs(self, input_signal):
        continue_propagation_threshold = 1
        if self.status == 'ready':
            self.signal += input_signal
            print ("{} input signal: {}".format(self.name, self.signal))
            if self.signal >= continue_propagation_threshold:
                self.signal = 0
                self.activate()

    def get_name(self):
        return self.name

    def get_activation_probability(self):
        return self.activation_probability

    def get_score(self):
        return self.score

    def get_connections(self):
        return self.connections

#### Dendrite Class starts #####
from nerve import Nerve

class Dendrite:
    def __init__(self, name, connection = None):
        self.name = name
        self.propagation_probability = 0.5
        self.signal = 0
        self.connection = self.__connection_initializer(connection)
        self.variability = 0.01

    def __connection_initializer(self, connection):
        if self.name == 'D0' and connection == None:
            V0 = Nerve('V0')
            return [V0]
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

    def clean(self, neuron_ap = None):
        stop_propagation_certainty = 0
        dead_neuron = 0
        temp_connections = []

        if neuron_ap == dead_neuron:
            self.connections = []
        else:
            for connection in self.connection:
                if connection.get_name()[0] == 'V':
                    if (self.propagation_probability > stop_propagation_certainty):
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
