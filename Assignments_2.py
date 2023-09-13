#1
Hours = float(input("Enter Hours : "))
Rate = float(input("Enter Rate : "))
print("Salary :",Hours * Rate)

#2
Celsius = float(input("Enter Celsius Temperature : "))
print("Fahrenheit Temperature : ", Celsius * 9 / 5 + 32)

#3
Seconds = int(input("Enter seconds : "))
print(Seconds,"seconds is",Seconds//3600,"hours,",(Seconds%3600)//60,"minutes,",(Seconds%3600)%60,"seconds")
