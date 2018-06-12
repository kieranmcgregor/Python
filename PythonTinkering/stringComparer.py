testString = input("Please enter a test string: ")
actualString = input("Please enter an actual string: ")
bitMask = []

def stringComparer(testString, actualString, bitMask):
	n = len(testString)//2
	m = len(actualString)//2

	if (n == 0 and m == 0):
		bitMask.append(testString == actualString)
		return bitMask
	elif(n == 0):
		stringComparer(testString, actualString[:m], bitMask)
		stringComparer(testString, actualString[m:], bitMask)
		return bitMask
	elif(m == 0):
		stringComparer(testString[:n], actualString, bitMask)
		stringComparer(testString[n:], actualString, bitMask)
		return bitMask
	else:
		stringComparer(testString[:n], actualString[:m], bitMask)
		stringComparer(testString[n:], actualString[m:], bitMask)

		return bitMask

stringComparer(testString, actualString, bitMask)
print(bitMask)
