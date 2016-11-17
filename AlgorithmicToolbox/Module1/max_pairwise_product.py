# Uses python3
import random

def max_pairwise_product():
#def max_pairwise_product(a):
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    maxInt = None
    max2ndInt = None

    for i in range(0, n):
#    for i in range(0, len(a)):
        
        if maxInt == None:
            maxInt = a[i]

        elif max2ndInt == None and a[i] > maxInt:
            max2ndInt = maxInt
            maxInt = a[i]

        elif max2ndInt == None and a[i] <= maxInt:
            max2ndInt = a[i]
 
        elif a[i] <= maxInt and a[i] > max2ndInt:
            max2ndInt = a[i]
 
        elif a[i] > maxInt:
            max2ndInt = maxInt
            maxInt = a[i]
 

    print(maxInt * max2ndInt)
    return maxInt, max2ndInt

max_pairwise_product()

##def randomArrayBuilder(size, max, min):
##    randomArray = []
##
##    while len(randomArray) < size:
##        randomArray.append(random.randrange(min, max))
##
##    return randomArray
##
##def pairwiseMaxTester(pairwiseMaxValue, array):
##
##    result = 0
##
##    for i in range(0, len(array)):
##        for j in range(i+1, len(array)):
##            if array[i]*array[j] > result:
##                result = array[i]*array[j]
##
##    print(result, pairwiseMaxValue, result == pairwiseMaxValue)
##    return result == pairwiseMaxValue
##        
##            
##            
##tester = True
##
##while(tester):
##    randomArray = randomArrayBuilder(100, 10, 0)
##    maxPairwiseList = max_pairwise_product(randomArray)
##    maxPairwiseProduct = maxPairwiseList[0] * maxPairwiseList[1]
##    tester = pairwiseMaxTester(maxPairwiseProduct, randomArray)
##    if not tester:
##        print(randomArray)
##        print(maxPairwiseList)
