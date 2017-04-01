import random

class Neuron:
    def __init__(self):
        self.divisor = 2.0
        self.signal = 0

    def get_divisor(self):
        return self.divisor

    def set_divisor(self, feedback):
        signal = self.signal
        if feedback == '+':
            if signal > 0:
                self.divisor += random.uniform(0, 0.1)
            elif signal < 0:
                self.divisor -= random.uniform(0, 0.1)
        elif feedback == '-':
            if signal > 0:
                self.divisor -= random.uniform(0, 0.1)
            elif signal < 0:
                self.divisor += random.uniform(0, 0.1)

    def get_signal(self):
        return self.signal

    def set_signal(self):
        x = 0.0
        y = 1.0
        divisor = self.divisor

        rand_float = random.uniform(x, y)

        if rand_float > y/divisor:
            self.signal = 1
        else:
            self.signal = -1

N1 = Neuron()
N2 = Neuron()

N1_divisor = N1.get_divisor()
print (N1_divisor)

N1.set_signal()
N2.set_signal()
N1_signal = N1.get_signal()
N2_signal = N2.get_signal()
print (N1_signal, N2_signal)

N1.set_divisor("+")
N1_divisor = N1.get_divisor()
N2_divisor = N2.get_divisor()
print (N1_divisor, N2_divisor)

count = 0
total = 0
while count < 100:
    N1.set_signal()
    N1_signal = N1.get_signal()
    if N1_signal == 1:
        total += 1

    count += 1

print ("+ sig: {}%\n- sig: {}%".format(total/count, (count-total)/count))
