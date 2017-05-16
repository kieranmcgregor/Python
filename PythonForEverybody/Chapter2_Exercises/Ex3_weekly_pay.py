hours_empty = True

while hours_empty:
    hours = input("How many hours did you work this week? (Please enter a number)\n")
    try:
        hours = float(hours)
        hours_empty = False
    except:
        print ("Invalid input, please enter a number")

rate_empty = True

while rate_empty:
    rate = input("What is your rate of pay per hour? (Please enter a number)\n")
    try:
        rate = float(rate)
        rate_empty = False
    except:
        print ("Invalid input, please enter a number")

pay = hours * rate

print ("Your pay for the week is {:.2f}".format(pay))
