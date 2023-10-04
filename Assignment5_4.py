while True:
    string_up = ""
    string = input("Please enter string: ")
    for i in string:
        if (i != ",") and (i != ".") and (i != ":") and (i != "!") and (i != "?"):
            string_up += i.upper()
    if string == "done":
        print("Bye !")
        break
    print(string_up)