def dnc_recur(array_1, array_2):
    half_1 = len(array_1)//2
    half_2 = len(array_2)//2

    array_11 = array_1[:half_1]
    array_12 = array_1[half_1:]

    array_21 = array_2[:half_2]
    array_22 = array_2[half_2:]

    if (len(array_1) == 1 & len(array_2) == 1):
        print (array_12, array_22)
        return (array_12, array_22)

    elif (half_1 == 0):
        return (dnc_recur(array_12, array_21),
                dnc_recur(array_12, array_22))

    elif (half_2 == 0):
        return (dnc_recur(array_11, array_22),
                dnc_recur(array_12, array_22))

    else:
        return (dnc_recur(array_11, array_21),
                dnc_recur(array_11, array_22),
                dnc_recur(array_12, array_21),
                dnc_recur(array_12, array_22))

array_1 = [1, 2, 3, 4, 5]
array_2 = [6, 7, 8, 9, 10, 11]

dnc_recur(array_1, array_2)
