from neuron import Neuron
from dendrite import Dendrite
from nerve import Nerve

def unit_tests():
    ### Construct two Neuron objects
    D1 = Dendrite()
    V1 = Nerve()
    N1 = Neuron()
    N2 = Neuron()

    N1.add_connection(D1)
    N2.add_connection(V1)

    total = 0
    count = 0

    while count < 50:
        N1.propagate()
        if D1.get_signal() == 1:
            V1_output = V1.get_output()
            print ("V1 ouput: {}".format(V1_output))
            total += 1
        count += 1

    print ("+ sig: {}%\n- sig: {}%\n*From Neuron"
            .format(total/count, (count-total)/count))

unit_tests()
