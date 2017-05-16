class Shop:

##   Common base class for shop

   def __init__(self):
      self.hardware_list = Hardware.hardware_list()
      self.software_list = Software.software_list()
      self.item_list = Item.item_list()

def shop():

    response = input ("Welcome to my humble shop, what brings you in here today?\nHardware\nSoftware\nItems\nNothing\n\n")

    while response != 'Hardware' or 'hardware' or 'Software' or 'software' or 'Items' or 'items' or 'Nothing' or 'nothing':
        response = input ("What was that? You seem to be mumbling.\nHardware\nSoftware\nItems\nNothing\n\n")
    
    if response == 'Hardware' or 'hardware':
        print (hardware_list)

    if response == 'Software' or 'software':
        print (software_list)

    if response == 'Items' or 'items':
        print (item_list)

    else:
        return "Well in that case, go loiter someplace else! I have customers to attend to!"

    buy = input ('So what you buying today?')

##    for buy in hardware_list or software_list or item_list:
        
