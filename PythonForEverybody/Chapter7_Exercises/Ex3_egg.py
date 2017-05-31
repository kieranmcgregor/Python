file_name_empty = True
file_name = ""

while file_name_empty:
    file_name = input("Please enter file name:\n")

    if file_name == "na na boo boo":
        print ("\nWhat are we five? Enter a damn file name!")
        continue
    else:
        try:
            fh = open(file_name)
            file_name_empty = False
        except:
            print ("File not found, please ensure file path is correct.")
            continue

criteria = "X-DSPAM-Confidence"
confidence_total = 0
count = 0

for line in fh:
    if criteria in line:
        start = line.find(":") + 1
        numstr = line[start:].strip()
        confidence_total += float(numstr)
        count += 1

avg = confidence_total/count

print("Average spam confidence: {}".format(avg))
