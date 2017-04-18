class PreDendrite:
    def __init__(self, name, connection):
        self.name = name
        self.connection = [connection]
        self.score = 1

    def adjust_score(self, feedback):
        if feedback == '+':
            self.score += 1
            print ("{} score: {}".format(self.name, self.score))
        elif feedback == '-':
            self.score -= 1
            print ("{} score: {}".format(self.name, self.score))

    def get_name(self):
        return self.name

    def get_connection(self):
        return self.connection

    def get_score(self):
        return self.score
