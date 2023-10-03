def num_divide3(num1):
    count = 0
    num1 += 1
    for i in range(1, num1):
        if (i % 3 == 0):
            count += 1
    return count
while True:
    num = (input("Enter a positive integer : "))
    try:
        num = int(num)
    except:
        if num == "done":
            print("bye!")
            break
        else:
            print("please enter a positive number")
            continue
    if (num > 0):
        print("numbers divisible by 3 among numbers from 1 to", num, " : ", num_divide3(num))
    else:
        print("please enter a positive number")