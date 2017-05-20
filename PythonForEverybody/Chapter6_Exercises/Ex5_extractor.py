string = 'X-DSPAM-Confidence:0.8475'

length= len(string)
num_start = string.find(':') + 1

number = float(string[num_start:length])

print(number, type(number))
