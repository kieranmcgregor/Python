import random
from predendrite import PreDendrite
from nd_meld import Dendrite

class Neuron:
    def __init__(self, name):
        self.name = name
        self.activation_probability = 0.5
        self.signal = 0
        self.connections = self.__connections_initializer()
        self.variability = 0.01
        self.predendrite_threshold = 1

    def __connections_initializer(self):
        D1 = Dendrite('D1')
        return [D1]

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

    def check_connections(self, neuron, feedback):
        for connection in self.connections:
            if connection.get_connection() == neuron:
                if type(connection) == Dendrite:
                    return False

                elif type(connection) == PreDendrite:
                    predendrite = connection
                    predendrite.adjust_score(feedback)
                    return False

        return True

    def add_predendrite(self, connection):
        predendrite_name = "P" + str(len(self.connections))
        new_predendrite = PreDendrite(predendrite_name, connection)
        self.connections.append(new_predendrite)

    def add_dendrite(self, connection):
        dendrite_name = "D" + str(len(self.connections))
        new_dendrite = Dendrite(dendrite_name, connection)
        self.connections.append(new_dendrite)

    def clean(self):
        temp_dendrites = []
        temp_predendrites = []

        for connection in self.connections:
            if type(connection) ==  Dendrite:
                dendrite = connection
                dendrite.clean(self.activation_probability)

                if len(dendrite.get_connection()) != 0:
                    temp_dendrites.append(dendrite)

            elif type(connection) == PreDendrite:
                predendrite = connection
                if predendrite.get_score() >= self.predendrite_threshold:
                    connection = predendrite.get_connection()
                    self.add_dendrite(connection)

                elif predendrite.get_score() > 0:
                    temp_predendrites.append(predendrite)

        self.connections = temp_predendrites + temp_dendrites

    def activate(self):
        for connection in self.connections:
            if type(connection) == Dendrite:
                dendrite = connection
                dendrite.propagate()

    def adjust_probability(self, feedback, state):
        self.__set_probability(feedback, state)
        print ("{} firing probability: {}"
                .format(self.name, self.activation_probability))
        print ("{} {}".format(self.name, self.connections))

        for connection in self.connections:
            if type(connection) == Dendrite:
                dendrite = connection
                dendrite.adjust_probability(feedback)

    def manage_inputs(self, input_signal):
        continue_propagation_threshold = 1
        self.signal += input_signal
        print ("Input signal: {}".format(self.signal))
        if self.signal >= continue_propagation_threshold:
            self.activate()

    def get_name(self):
        return self.name

    def get_activation_probability(self):
        return self.activation_probability

    def get_score(self):
        return self.score

    def get_connections(self):
        return self.connections

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
