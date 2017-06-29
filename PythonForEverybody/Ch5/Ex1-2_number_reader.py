live = True
max_num = None
min_num = None
total = 0
count = 0

while live:
    number = input("Enter a number or 'done' to exit: ")

    try:
        number = float(number)
    except:
        if type(number) == str:
            if 'done' in number.lower():
                live = False
            else:
                print("Invalid input, please enter a number")

            continue

    total += number
    count += 1

    if max_num == None or number > max_num:
        max_num = number

    if min_num == None or number < min_num:
        min_num = number

if count > 0:
    print ("Total: {}\nCount: {}\nAverage: {}".format(total, count, (total/count)))
    print ("Max: {}\nMin: {}".format(max_num, min_num))
else:
    print ("Total: {}\nCount: {}\nAverage: undefined".format(total, count))
