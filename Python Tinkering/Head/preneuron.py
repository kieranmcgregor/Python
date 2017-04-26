from nd_meld import Dendrite
class PreNeuron:
    def __init__(self, name, connections):
        self.__name = name
        self.__dendrite_count = 0
        self.__connections = self.__connection_initializer(connections)
        self.__score = 1

    def __connection_initializer(self, connections = None):
        dendrite_name = ''
        dendrite_name = "D" + str(self.__name[1:]) + str(self.__dendrite_count)
        self.__dendrite_count += 1
        new_dendrite = Dendrite(dendrite_name, connections)
        return [new_dendrite]

    def adjust_score(self, feedback):
        if feedback == '+':
            self.__score += 1
            print ("{} score: {}".format(self.__name, self.__score))
        elif feedback == '-':
            self.__score -= 3
            print ("{} score: {}".format(self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_connections(self):
        return self.__connections

    def get_score(self):
        return self.__score
