class Hardware:

##   Common base class for harware

   def __init__(self):
      self.hardware_list = Hardware.hardware_list()


def hardware_list():
    hardware_list = []

    name = 'Stick'
    strength = 3
    cost = 10
    stick_trait = [name, strength, cost]
    hardware_list.append(stick_trait)
