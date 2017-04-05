from neuron import Neuron
from dendrite import Dendrite
from nerve import Nerve

def unit_tests():
    ### Construct two Neuron objects
    D1 = Dendrite("D1")
    V1 = Nerve("V1")
    V2 = Nerve("V2")
    N1 = Neuron("N1")
    N2 = Neuron("N2")

    N1.add_connection(D1, N2)
    N1.add_connection(V1)
    N2.add_connection(V2)

    total = 0
    count = 0

    while count < 50:
        N1.self_propagate()
        if D1.get_signal() == 1:
            total += 1
        count += 1

    print ("+ sig: {}%\n- sig: {}%\n*From Neuron"
            .format(total/count, (count-total)/count))

unit_tests()
