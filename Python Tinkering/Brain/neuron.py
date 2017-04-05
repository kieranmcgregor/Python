# from dendrite import Dendrite
# from nerve import Nerve

class Neuron:
    def __init__(self, name):
        self.name = name
        self.signal = 0
        self.score = 0
        self.connections = []

    def add_connection(self, connection, neuron = None):
        self.connections.append(connection)
        if neuron != None:
            connection.add_connection(Neuron)

    def self_propagate(self):
        for connection in self.connections:
            connection.propagate()

        self.adjust_score()

    def group_propagate(self):
        for connection in self.connections:
            connection.propagate()

    def adjust_score(self):
        feedback = input("Reward or punish? (+ / -) ")

        if feedback == "+":
            self.score = 0
        elif feedback == "-":
            self.score += 1
        print ("{} score: {}".format(self.name, self.score))

        for connection in self.connections:
            connection.adjust_score(feedback)

    def manage_inputs(self, input_signal):
        signal = self.signal
        signal += input_signal
        print ("Input signal: {}".format(signal))
        if signal >= 1:
            self.group_propagate()

    def get_score(self):
        return self.score

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
