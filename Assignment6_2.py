fhand = open("C:/Users/fr0ze/Documents/GitHub/Computational-Thinking-and-Programming/mbox.txt","r")
count = 0
for line in fhand:
    if line.startswith("From:"):
        a = line.find("@")
        b = line.find(" ", a)
        print(line[a+1:b])
        count += 1
print("Total %d hosts printed" %(count))
fhand.close()
