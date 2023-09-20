sum = 0
count = 0
while True:
    num = (input("Enter a number : "))
    try:
        num = int(num)
    except:
        if num == "done":
            break
        else:
            print("invalid input. enter a number")
            continue
    sum+=num
    count+=1
average = sum/count
print("Sum of input numbers : ", sum)
print("Number of input : ", count)
print("Average of input numbers : ", average)