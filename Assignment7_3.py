fhand = open("C:/Users/fr0ze/Documents/GitHub/Computational-Thinking-and-Programming/mbox.txt","r")
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[1])
    count = count + 1
print("Total %d lines were printed" % count)