name = input ('Name: ')
age = input ('Age: ')
height = input ('Height in cm: ')
weight = input ('Weight in kg: ')
waist_circ = input ('Waist circumference in cm: ')
active_level= input ('Activity level from 0 (worst) to 5 (best): ')

##age = 33
##height = 173
##weight = 73
##waist_circ = 81.2
##activ_level = 4

## Calculates player's percent_bf using player's waist circumference and weight
POUNDS_PER_KILOGRAM = 2.2
CENTIMETERS_PER_INCH = 2.54
PERCENT_TO_NUMBER = 100
THE_SCIENTIST_SAIDSO = -98.42
I_DONT_KNOW0 = 4.15
I_DONT_KNOW1 = 0.082

def long_form():
    percent_bf = PERCENT_TO_NUMBER * (THE_SCIENTIST_SAIDSO + I_DONT_KNOW0 * (float(waist_circ)/CENTIMETERS_PER_INCH) - I_DONT_KNOW1 * float(weight)*POUNDS_PER_KILOGRAM)/(float(weight)*POUNDS_PER_KILOGRAM)
    return percent_bf

def step_form():
    percent_bf0 = float(weight)*POUNDS_PER_KILOGRAM/float(weight)*POUNDS_PER_KILOGRAM
    percent_bf0 = percent_bf0 * I_DONT_KNOW1
    percent_bf1 = I_DONT_KNOW0 * (float(waist_circ)/CENTIMETERS_PER_INCH)
    percent_bf = PERCENT_TO_NUMBER * (THE_SCIENTIST_SAIDSO + percent_bf1 - percent_bf0)
    return percent_bf
