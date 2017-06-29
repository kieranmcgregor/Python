score_empty = True
score_max = 1.0
score_min = 0.0

while score_empty:
    score = input("Enter a score between 0.0 and 1.0: (Please enter a number)\n")
    try:
        score = float(score)
        score_empty = False
    except:
        print ("Invalid input, please enter a number")
        continue

    if score > score_max:
        print ("Invalid entry, maximum score is 1.0.")
        score_empty = True

    elif score < score_min:
        print ("Invalid entry, minimum score is 0.0.")
        score_empty = True

    elif score >= 0.9:
        print ('A')

    elif score >= 0.8:
        print ('B')

    elif score >= 0.7:
        print ('C')

    elif score >= 0.6:
        print ('D')

    elif score < 0.6:
        print ('F')
