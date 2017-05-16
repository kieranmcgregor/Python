hours_empty = True
full_time_max = 40
overtime_premium = 1.5

def computepay(hours, rate):

    if hours <= full_time_max:
        pay = hours * rate

    elif hours > full_time_max:
        pay = full_time_max * rate
        pay += (hours - full_time_max) * (rate * overtime_premium)

    return pay

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

pay = computepay(hours, rate)

print ("Your pay for the week is {:.2f}".format(pay))
