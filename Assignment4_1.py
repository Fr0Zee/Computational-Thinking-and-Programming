def grade_calc(score1):
    if score1 >= 90:
        return("A")
    elif score1 >= 80:
        return("B")
    elif score1 >= 70:
        return("C")
    elif score1 >= 60:
        return("D")
    else:
        return("F")

try:
   score = int(input("Enter score : "))
except:
   print("Error, please enter numeric input between 0 and 100")
else:
    if (score>=0) & (score<=100):
        print("Grade is",grade_calc(score))
    else:
        print("Error, please enter numeric input between 0 and 100")