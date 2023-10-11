fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened :", fname)
else:
    count = 0
    sum = 0
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            a = line.split()
            b = a[1]
            sum += float(b)
            count += 1
    if count != 0:
        average = sum/count
    print("Average spam confidence :",average)