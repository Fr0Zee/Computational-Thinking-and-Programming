string = input("Please enter string: ")
UpperC_letters = 0
LowerC_letters = 0
Numbers = 0
Other = 0
for i in string:
    if i.isupper():
        UpperC_letters += 1
    elif i.islower():
        LowerC_letters += 1
    elif i.isdigit():
        Numbers += 1
    else:
        Other += 1
print("-  Uppercase Letters:",UpperC_letters)
print("-  Lowercase Letters:",LowerC_letters)
print("-  Numbers:",Numbers)
print("-  Other characters:",Other)