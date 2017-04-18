import random

class Nerve:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.output = self.__set_output()

    def __set_output(self):
        canvas_width = 128
        canvas_height = 128
        rgb_index = 0
        intensity = 0

        alpha = random.randint(0, 255)
        if alpha > 0:
            rgb_index = random.randint(0, 2)
            intensity = random.randint(0, 255)

        x_pos = random.randint(0, canvas_width)
        y_pos = random.randint(0, canvas_height)

        return ((x_pos, y_pos), (rgb_index, intensity, alpha))

    def propagate(self):
        print ("{} Output: {}".format(self.name, self.output))

    def adjust_score(self, feedback):
        if feedback == "+":
            self.score = 0
        elif feedback == "-":
            self.score += 1
        print ("{} score: {}".format(self.name, self.score))

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_output(self):
        return self.output

# def unit_tests():
#     ### Construct two Dendrite objects
#     V1 = Nerve()
#     V2 = Nerve()
#
#     ### Get signal for Nerves V1 and V2 should equal 1
#     V1_signal = V1.get_signal()
#     V2_signal = V2.get_signal()
#     print ("V1 signal: {}\nV2 signal: {}"
#             .format(V1_signal, V2_signal))
#
#     ### Check Nerve V1 and V2's output details which should be a randomly
#     ### created multi-dimensional tuple of
#     ### ((pos_x, pos_y), (rgb_index, intensity, alpha))
#     V1_output = V1.get_output()
#     V2_output = V2.get_output()
#     print ("V1 ouput: {}\nV2 output: {}"
#             .format(V1_output, V2_output))
#
#     ### Check propgate function which is incomplete (2017 04 01 23:40)
#     V1.propagate()
#
# unit_tests()
