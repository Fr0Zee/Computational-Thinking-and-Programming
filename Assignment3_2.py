try:
   score = int(input("Enter score : "))
except:
   print("Error, please enter numeric input between 0 and 100")
else:
   if (score>=0) & (score<=100):
       print("Grade is",end=" ")
       if score >= 90:
           print("A")
       elif score >= 80:
           print("B")
       elif score >= 70:
           print("C")
       elif score >= 60:
           print("D")
       else:
           print("F")
   else:
       print("Error, please enter numeric input between 0 and 100")