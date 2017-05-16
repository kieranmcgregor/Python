import sys

def prime_point_calc(numerator, denominator):
    # Returns a number if it is a prime number
    prime = True
    while denominator < numerator:
        if (numerator % denominator) == 0:
            prime = False
            break
        else:
            denominator += 1

    if prime:
        return numerator

def prime_list_calc(numerator_limit, denominator):
    # Returns list of prime numbers from 1 to user defined limit
    primes = [1, 2]
    numerator = 3
    while numerator <= numerator_limit:

        prime = prime_point_calc(numerator, denominator)
        if prime != None:
            primes.append(prime)

        if denominator == numerator:
            denominator == 0
        numerator += 1

    return primes

def prime_start_calc(start, denominator):
    # Returns next prime after given user input
    not_prime = True
    prime = 0
    numerator = start

    while not_prime:
        prime = prime_point_calc(numerator, denominator)
        if prime != None:
            not_prime = False
        numerator += 1

    return prime

def main():
    numerator_empty = True
    lps_empty = True
    denominator = 2
    prime = None
    primes = None

    print ("\nThis program will calculate prime numbers.")

    while numerator_empty:
        numerator = input("Please enter an integer: ")
        try:
            numerator = int(numerator)
            numerator_empty = False
        except:
            print ("Invalid entry, not an integer.")

    while lps_empty:
        lps = input("Is this number a [l]imit, a [p]oint or a [s]tart? ")
        if lps != 'l' and lps != 'p' and lps != 's':
            print("Invalid entry, type 'l' for limit, 'p' for point or 's' for start.")
        else:
            lps_empty = False


    if numerator > sys.maxsize:
        numerator = sys.maxsize - 10

    if lps[0].lower() == 'l':
        numerator_limit = numerator
        primes = prime_list_calc(numerator_limit, denominator)

    elif lps[0].lower() == 'p':
        prime = prime_point_calc(numerator, denominator)

    elif lps[0].lower() == 's':
        start = numerator
        prime = prime_start_calc(start, denominator)

    if prime != None:
        print ("{} is a prime number.".format(prime))
    elif primes != None:
        print ("The following numbers are primes.\n{}".format(primes))
    elif prime == None:
        print ("{} is not a prime number.".format(numerator))

main()
