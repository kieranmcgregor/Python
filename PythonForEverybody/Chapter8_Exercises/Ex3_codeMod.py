fname = '../Files/mbox-short.txt'
print (fname)
fhand = open(fname)
count = 0

for line in fhand:
    words = line.split()

    if len(words) == 0 or words[0] != 'From': continue
    if len(words) < 3: continue
    print (words[2])
