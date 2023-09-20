try:
   hours = int(input("Enter hours: "))
   rate = int(input("Enter rate: "))
except:
   print ("Error, please enter numeric input")
else:
   if hours > 40:
       dif = hours - 40
       print("Pay :",((dif*1.5*rate)+((hours-dif)*rate)))
   else:
       print("Pay :",(hours*rate))