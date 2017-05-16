##class Player_character:

print ('Welcome fleshy bag of water, please enter you details.\n')

##def player_character():
name = input ('Name: ')
age = input ('Age: ')
height = input ('Height in cm: ')
weight = input ('Weight in kg: ')
waist_circ = input ('Waist circumference in cm: ')
active_level= input ('Activity level from 0 (worst) to 5 (best): ')

## Calculates player's percent_bf using player's waist circumference and weight
POUNDS_PER_KILOGRAM = 2.2
CENTIMETERS_PER_INCH = 2.54
PERCENT_TO_NUMBER = 100
THE_SCIENTIST_SAIDSO = -98.42
I_DONT_KNOW0 = 4.15
I_DONT_KNOW1 = 0.082

percent_bf = PERCENT_TO_NUMBER * (THE_SCIENTIST_SAIDSO + I_DONT_KNOW0 * (float(waist_circ)/CENTIMETERS_PER_INCH) - I_DONT_KNOW1 * float(weight)*POUNDS_PER_KILOGRAM)/(float(weight)*POUNDS_PER_KILOGRAM)
##percent_bf0 = float(weight)*POUNDS_PER_KILOGRAM/float(weight)*POUNDS_PER_KILOGRAM
##percent_bf0 = percent_bf0 * I_DONT_KNOW1
##percent_bf1 = I_DONT_KNOW0 * (float(waist_circ)/CENTIMETERS_PER_INCH)
##percent_bf = PERCENT_TO_NUMBER * (THE_SCIENTIST_SAIDSO + percent_bf1 - percent_bf0)

##  Determines the number of hit points for players character based on their percent_bf

if percent_bf >= 8 and percent_bf <= 12:
    hit_points = 300

elif percent_bf >=8 and percent_bf <= 13:
    hit_points = 280

elif percent_bf >=7 and percent_bf <= 15:
    hit_points = 260

elif percent_bf >=7 and percent_bf <= 17:
    hit_points = 240

elif percent_bf >=6 and percent_bf <= 19:
    hit_points = 220

elif percent_bf >=6 and percent_bf <= 20:
    hit_points = 200

elif percent_bf >=5 and percent_bf <= 21:
    hit_points = 180

elif percent_bf >=5 and percent_bf <= 23:
    hit_points = 160

elif percent_bf >=4 and percent_bf <= 25:
    hit_points = 140

elif percent_bf >=4 and percent_bf <= 27:
    hit_points = 120

elif percent_bf >=3 and percent_bf <= 29:
    hit_points = 100

elif percent_bf >=3 and percent_bf <= 31:
    hit_points = 80

elif percent_bf >=2 and percent_bf <= 32:
    hit_points = 60

elif percent_bf <=2 or percent_bf >= 32:
    hit_points = 40

## Determine character's reaction time based on player's activity level

active_level = int(active_level)

react_time = 10 - active_level * 2

## Determine character's attack strength based on their BMI
BMI_ADJUSTMENT = 703

attack_str = (int(weight)*POUNDS_PER_KILOGRAM/ (int(height)/CENTIMETERS_PER_INCH) ** 2)
attack_str = attack_str * BMI_ADJUSTMENT
attact_str = int(attack_str)

accuracy = 80

dodge = 80

traits = [name, age, height, weight, waist_circ, active_level, hit_points, react_time, attack_str, accuracy, dodge]

gold = 0
math_skill = 0
health_points = 0

wares = [gold, math_skill, health_points]

print ('\nIf you\'re looking for a fight enter "fight()".\nWhat\'s the matter Colonel Sanders? Chicken!')

##def player_details():
##    print ('')
##    print ("Name: " + name)
##    print ('Age: ' + age)
##    print ('Height: ' + height)
##    print ('Weight: ' + weight)
##    print ('Waist circumference: ' + waist_circ)
##    print ('Activity level: ' + str(activ_level))
##    print (' ')
##    print ('VITALS')
##    print ('Hit points: ' + str(hit_points))
##    print ('Reaction time: ' + str(react_time) + " seconds")
##    print ('Attack strength: ' + str(attack_str))
##    print ('Dodge ability: ' + str(dodge))
##    print ('Escape percentage: ' + str(esc_percent))
##    print (' ')
##    print ('SKILLS')
##    print ('Math: N/A')
##    print ('Physics: N/A')
##    print ('Biology: N/A')
##    print ('Language: N/A')
def shop ():
    import Shop
    Shop.shop()
    

def fight ():

    print ('\nThem\'s fighten words!\n')
    import Enemy1
    enemy = Enemy1.random_enemy()

## A fight loop that will continue until either the player or enemy has no more hit points

    while (traits[6] > 0 and enemy[1] > 0):

        ## A selection loop that will continue until the player selects valid desired actions
        
        action = input ('\nWhat shall we do Captain Thunderpants?\n\nMath     Phys\nChem     Lang\n')

        while not (action == 'Math'):
            action = input ('\nWhat is your major malfunction Private Pile?\n\nMath     Phys\nChem     Lang\n')
        action1 = input ('\nEasy like your mother, which one?\n\nCount     Add\n')

        while not (action1 == 'Count' or 'Add'):
            action1 = input ('\nWow! Here\'s hoping you win a Darwin Award?\n\nCount     Add\n')

        if action1 == 'Add':
            rounds = 5
            damage = 0

            ## An attack loop that uses the appropriate mechanism for the players attack selection and continues until the player runs out of rounds.
            ## It provides a sequence of numbers that start at a random point and are summed using a random difference.

            while rounds >0:
                print ('\nGIVER!!!\n')

                import random
                random_start = random.randrange(1, 100+1)
                difference = random.randrange(1, 10+1)
                print (str(random_start) + '\n' + str(random_start + difference) + '\n' + str(random_start + difference*2) + '\n' + str(random_start + difference*3) + '\n')
                answer = input ('\nWhat\'s next slugger?\n')

                ## Provides the outcome of the attack in the round and accumulates any necessary damage points to be
                ## subtracted from the enemy hit points.
                
                if str(answer) == str(random_start + difference*4):
                    print ('\nCan we kick it? Yes, we can!\n')

                    hit = random.randrange(0, 100+1)
                    evade = random.randrange(0, 100+1)
                    
                    if hit > (traits[-2]):
                        print ('\nYou couldn\'t hit the ground if it weren\'t for gravity!\n')
                        rounds = rounds - 1
                    elif evade <= enemy[3]:
                        print ('\nToo slow gramps! Looks like he\'s a slippery one\n')
                        rounds = rounds - 1
                    else:
                        damage = damage + random.randrange(int(traits[-3]-10), int(traits[-3]))
                        rounds = rounds - 1

                else:
                    print ('\nYou shit the bed on that one champ!\n')
                    rounds = rounds - 1

            enemy[1] = enemy[1] - damage

        elif action1 == 'Count':
            rounds = 5
            damage = 0

            ## An attack loop that uses the appropriate mechanism for the players attack selection and continues until the player runs out of rounds.
            ## It provides a sequence of numbers that start at a random point and are summed using a random difference.

            while rounds >0:
                print ('\nGIVER!!!\n')

                import random
                random_start = random.randrange(1, 100+1)
                print (str(random_start) + '\n' + str(random_start+1) + '\n' + str(random_start+2) + '\n' + str(random_start+3))
                answer = input ('\nWhat\'s next slugger?\n')

                ## Provides the outcome of the attack in the round and accumulates any necessary damage points to be
                ## subtracted from the enemy hit points.


                if str(answer) == str(random_start + 4):
                    print ('\nCan we kick it? Yes, we can!')

                    hit = random.randrange(0, 100+1)
                    evade = random.randrange(0, 100+1)
                    
                    if hit > (traits[-2]):
                        print ('But you missed. You couldn\'t hit the ground if it weren\'t for gravity!')
                        rounds = rounds - 1
                    elif evade <= enemy[3]:
                        print ('But you\'re too slow gramps! Looks like he\'s a slippery one.')
                        rounds = rounds - 1
                    else:
                        damage = damage + random.randrange(int(traits[-3]-10), int(traits[-3]))
                        rounds = rounds - 1

                else:
                    print ('\nYou shit the bed on that one champ!\n')
                    rounds = rounds - 1
                    
            enemy[1] = enemy[1] - damage

        ## Provide player with feedback on total damage done to enemy and execute enemy counter attack

        if enemy[1] > 0:
            print ('\nWell look at you! The ' + enemy[0] + ' now has ' + str(enemy[1]) + ' hp.')
            print ('But it looks like you pissed it off flesh bag. I hope you\'re good at dodging.')

            enemy_hit = random.randrange(0, 100+1)
            friendly_evade = random.randrange(0, 100+1)
            
            if enemy_hit > (enemy[4]):
                print ('\nWow! See that? This monster\'s got shit aim!')
            elif friendly_evade <= (traits[-1]):
                print ('\nOoooh, you are fast!')
            else:
                friendly_damage = random.randrange((int(enemy[2])-10), int(enemy[2]))
                traits[6] = traits[6] - friendly_damage
                print('\nIf you can dodge a wrench you can dodge a ball.\nApparently, you can\'t dodge either.')
            print ('\nYou now have ' + str(traits[6]) + ' hp.')

    ## Provide player with feedback about state of the enemy throught various comments based on overkill.
    ## Overkill is the number of hit points beyond beyond 0 the player managed
                
    if hit_points <= 0:
        print ('\nYou\'re dead sucker! Not a great way to end the day!')
        
    elif enemy[1] <= 0:
        
        if enemy[1] >= -10:
            print ('\nYou sure it\'s dead? Should we poke it with a stick?\nOh! Wait, no, it\'s definitely dead. It shit itself!\nGrab the gold and let\'s GTFO!')

        elif enemy[1] >= -30:
            print ('\nNot bad! A severed head mean\'s dead! Now, let\'s tomb\nraid that shit!\n')

        elif enemy[1] >= -65:
            print ('\nOh god! Blood is everywhere! If I had a stomach I\'d puke\non it\'s loafers. Speaking of which we should probably take those.')
            
        else:
            print ('\nHoly shit!! Did you see that thing\'s head explode!! We\'ll\nbe picking brains out of his wares for months!\nYou\'d be surprised where brain can get!')

    ## Increment players gold, skill points and health points accoring to enemies strength

    wares[0] = int(wares[0]) + 10
    wares[1] = int(wares[1]) + 10
    wares[-1] = int(wares[-1]) + 10
    print ('\nYou now have ' + str(wares[0]) + ' gold.')
    print ('Your Math Skill is now ' + str(wares[1]) + ' points.')
    print ('Your Health Points are now ' + str(wares[-1]) + ' points.')
    return 'What\'s next meat bag?'
