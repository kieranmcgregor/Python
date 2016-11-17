def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1
values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

def sum_odd_numbers(number1, number2):
    '''(int, int) -> int

    Returns the sum of odd numbers between and including number1 and number2

    >>>sum_odd_numbers(1, 5)
    9
    >>>sum_odd_numbers(7, 13)
    40

    PRECONDITION = The first number must be odd
    '''

    lst_odd = []
    i = 0
    
    while (number1+i) <= number2:
        value = number1 + i
        lst_odd.append(value)
        i = i+2

    return sum(lst_odd)
