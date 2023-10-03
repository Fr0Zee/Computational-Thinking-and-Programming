def compute_pay(hour1, rate1):
   if hours > 40:
       dif = hours - 40
       return((dif*1.5*rate)+((hours-dif)*rate))
   else:
       return(hours*rate)
try:
   hours = float(input("Enter hours: "))
   rate = float(input("Enter rate: "))
except:
   print ("Error, please enter numeric input")
else:
    print("Pay:",compute_pay(hours,rate))