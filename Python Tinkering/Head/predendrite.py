class PreDendrite:
    def __init__(self, name, connections):
        self.__name = name
        self.__connections = connections
        self.__score = 1

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
