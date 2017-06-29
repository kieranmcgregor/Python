score_empty = True
score_max = 1.0
score_min = 0.0

def computegrade(score):
    if score > score_max:
        return ('GT')

    elif score < score_min:
        return ('LT')

    elif score >= 0.9:
        return ('A')

    elif score >= 0.8:
        return ('B')

    elif score >= 0.7:
        return ('C')

    elif score >= 0.6:
        return ('D')

    elif score < 0.6:
        return ('F')


while score_empty:
    score = input("Enter a score between 0.0 and 1.0: (Please enter a number)\n")
    try:
        score = float(score)
        score_empty = False
    except:
        print ("Invalid input, please enter a number\n")
        continue

    grade = computegrade(score)

    if grade == 'GT':
        print ("Invalid entry, maximum score is 1.0.\n")
        score_empty = True
    elif grade == 'LT':
        print ("Invalid entry, minimum score is 0.0.\n")
        score_empty = True


print(grade)
