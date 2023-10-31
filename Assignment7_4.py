List = []
count = 0
while True:
    num = input("Please enter an integer : ")
    try:
        num = int(num)
    except:
        if num == "done":
            print("---------- Bye !! --------------")
            break
        continue
    else:
        List.append(num) 
        print(List,", average =", sum(List)/len(List))   