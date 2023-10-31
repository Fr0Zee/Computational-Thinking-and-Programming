fhand = open("C:/Users/fr0ze/Documents/GitHub/Computational-Thinking-and-Programming/romeo.txt","r")
List = []
for line in fhand:
    line = line.split()
    for word in line:
        if word not in List:
            List.append(word)
List = sorted(List)
print (List)
fhand.close()