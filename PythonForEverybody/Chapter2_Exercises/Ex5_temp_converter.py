celsius_empty = True
print("This program converts Celsius to Fahrenheit for all you yanks.")

while celsius_empty:
    celsius = input("Please enter a temperature in Celsius.\n")
    try:
        celsius = float(celsius)
        celsius_empty = False
    except:
        print ("Invalid entry, please enter a number.")

fahrenheit = celsius * (9/5) + 32

print ("{:.2f} C is equivalent to {:.2f} F.".format(celsius, fahrenheit))
