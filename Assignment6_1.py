fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened :", fname)
else:
    for line in fhand:
        print(line.upper().rstrip())
    fhand.close()
